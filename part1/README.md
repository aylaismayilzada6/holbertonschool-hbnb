# HBnB Evolution – Technical Architecture Documentation

## 1. Introduction

**HBnB Evolution** is a simplified AirBnB-like platform that enables users to:

* Register and manage accounts
* List and manage properties (places)
* Leave reviews
* Manage amenities associated with places

This document provides a **complete technical blueprint** of the system and is intended to guide development, testing, and future scalability.

It includes:

* System architecture (3-layer design)
* Business Logic layer (entities and relationships)
* Interaction flow between components

All diagrams follow **UML standards** and are designed for clarity and maintainability.

---

## 2. High-Level Architecture

The system follows a **three-layered architecture**:

### 🔹 Layers Overview

| Layer                    | Description                                      |
| ------------------------ | ------------------------------------------------ |
| **Presentation Layer**   | Handles API endpoints, services, and controllers |
| **Business Logic Layer** | Contains core logic and domain models            |
| **Persistence Layer**    | Manages data storage through repositories        |

---

### 🔹 Architecture Design

* The **Presentation Layer** communicates with the **Business Logic Layer**
* The **Business Logic Layer** processes logic and delegates storage operations
* The **Persistence Layer** interacts directly with the **Database**

---

### 🔹 Facade Pattern

The Presentation layer uses a **facade approach** to interact with the Business Logic layer.

✔ Benefits:

* Simplifies communication
* Reduces coupling
* Hides internal complexity

---

## 📦 High-Level Package Diagram

### 🔍 Explanation

* **Presentation**

  * API, Services, Controllers
  * Handles requests and responses

* **Business Logic Layer**

  * Contains logic modules:

    * `UserLogic`
    * `PlaceLogic`
    * `ReviewLogic`
    * `AmenityLogic`

* **Persistence Layer**

  * Repositories:

    * `UserRepository`
    * `PlaceRepository`
    * `ReviewRepository`
    * `AmenityRepository`

* **Database**

  * Stores all application data

---

## 3. Business Logic Layer

### 📊 Detailed Class Diagram

This layer defines the **core entities** and their relationships.

---

### 🔹 Entities

#### **User**

Represents a system user.

**Attributes:**

* id (UUID)
* fname, lname
* email
* password
* is_admin
* created_at, updated_at

**Methods:**

* register()
* update_profile()
* delete_account()

---

#### **Place**

Represents a property listing.

**Attributes:**

* id (UUID)
* title
* description
* price 
* latitude
* longitude

**Methods:**

* create()
* update()
* delete()

---

#### **Review**

Represents user feedback.

**Attributes:**

* id (UUID)
* rating
* comment
* created_at, updated_at

**Methods:**

* create()
* update()
* delete()

---

#### **Amenity**

Represents a feature (e.g., Wi-Fi, Parking).

**Attributes:**

* id (UUID)
* name
* description
* created_at, updated_at

**Methods:**

* create()
* update()
* delete()

---

### 🔗 Relationships 

* **User → Place**
  `1 → many`
  A user owns multiple places

* **User → Review**
  `1 → many`
  A user writes multiple reviews

* **Place → Review**
  `1 → many`
  A place can have multiple reviews

* **Place ↔ Amenity**
  `many ↔ many`
  A place includes multiple amenities, and an amenity can belong to multiple places

---

## 4. API Interaction Flow

The system follows a consistent interaction pattern:

```text
Client → Presentation → Business Logic → Persistence → Database → Response
```

