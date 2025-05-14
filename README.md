---

# The ShelfOrbit

---


An interactive web application to discover, search, and discuss books seamlessly. Built using Django, Django REST Framework, and React.js, it integrates book discovery, recommendations, and real-time chat into a single platform.

<div align="center">
  <img src="img/home page.gif" alt="Home Page" width="600" height="338">
</div>

---

## Discovering Books

Users can explore personalized book recommendations based on their preferences such as favorite genres, tags, or authors.

### Recommendations based on Themes

<div align="center">
  <img src="img/vibe gif.gif" alt="Recommendations by Genre and Tag" width="600" height="338">
</div>

### Recommendations based on Favorite Authors

<p align="center">
  <table>
    <tr>
      <td align="center">
        <strong>Recommendations based on Favorite Author</strong><br>
        <img src="img/fav author.png" alt="Recommendations by Favorite Author" width="475">
      </td>
      <td align="center">
        <strong>Recommendations based on Genre and Tag</strong><br>
        <img src="img/vibe.png" alt="Recommendations by Vibe" width="475">
      </td>
    </tr>
  </table>
</p>

### Search Books and Get Similar Book Recommendations

Users can search for a book, and the app will suggest books with similar genres, tags, or theme.

<div align="center">
  <img src="img/searchnsimilar.gif" alt="Search and Similar Books" width="600" height="338">
</div>

---

## UI Overview

Explore a curated list of books and dive into detailed insights for each one. The interface offers two main views:

**Book List and Detail View**

<p align="center">
  <table>
    <tr>
      <td align="center" width="480">
        <strong>Book List View</strong><br>
        <img src="img/Book List.gif" alt="Book List View" width="100%">
      </td>
      <td align="center" width="480">
        <strong>Book Detail View</strong><br>
        <img src="img/Book Details.gif" alt="Book Details View" width="100%">
      </td>
    </tr>
  </table>
</p>

 **Library List and Detail View**

View all libraries, their locations, and detailed book availability inside each library.

<div align="center">
  <img src="img/Lib List and Detail.gif" alt="Library List and Detail" width="475">
</div>

---

## Admin Panel - Django

Django Admin panel is used to manage books, libraries, users, and more.

<div align="center">
  <img src="img/Admin Panel.gif" alt="Admin Panel with Book and Library models" width="475">
</div>

---

## API Management - Django REST Framework

APIs are created using Django REST Framework to support frontend integration and external access.

 **API Root View**

Displays the root endpoints available for the API.

<div align="center">
  <img src="img/14.png" alt="API Root" width="475">
</div>

#### Book & Library API View
<p align="center">
  <table>
    <tr>
      <td align="center" width="480">
        <strong>Book API View</strong><br>
        <img src="img/Book DRF.gif" alt="Book DRF API View" width="100%">
      </td>
      <td align="center" width="480">
        <strong>Library API View</strong><br>
        <img src="img/Library DRF.gif" alt="Library DRF API View" width="100%">
      </td>
    </tr>
  </table>
</p>

---

## Book Discussion Platform 
**Real-time Chat Room**
BookShelf includes a React-based real-time chat platform where users can join discussion rooms and interact.

<p align="center">
  <table>
    <tr>
      <td align="center" width="480">
        <strong>Sign In / Sign Out</strong><br>
        <img src="img/sigin or signout.gif" alt="Sign In or Sign Out" width="100%">
      </td>
      <td align="center" width="480">
        <strong>Join or Leave Room</strong><br>
        <img src="img/join or leave room.gif" alt="Join or Leave Chat Room" width="100%">
      </td>
    </tr>
  </table>
</p>

#### Book Discussion Rooms

React-based real-time chat room for discussing books with other users.

<div align="center">
  <img src="img/chat gif.gif" alt="Book Chat Room" width="600" height="338">
</div>

---
---