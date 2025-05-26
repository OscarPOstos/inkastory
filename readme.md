# 📖 InkaStory API

**InkaStory** es una API RESTful para crear, jugar y seguir el progreso de historias interactivas basadas en decisiones. Diseñada con Django y Django REST Framework, permite a los usuarios explorar nodos narrativos, tomar decisiones y completar historias ramificadas.

---

## 🚀 Endpoints

### 📚 Historias
- `GET /api/stories/` — Lista todas las historias.
- `POST /api/stories/` — Crea una nueva historia.
- `GET /api/stories/{id}/` — Detalles de una historia.
- `PUT /api/stories/{id}/` — Actualiza una historia.
- `DELETE /api/stories/{id}/` — Elimina una historia.

---

### 🧩 Nodos de Historia (Story Nodes)
- `GET /api/stories/{story_id}/nodes/` — Lista todos los nodos de una historia.
- `POST /api/stories/{story_id}/nodes/` — Crea un nodo nuevo para la historia.
- `GET /api/nodes/{id}/` — Detalles de un nodo específico.
- `PUT /api/nodes/{id}/` — Actualiza un nodo.
- `DELETE /api/nodes/{id}/` — Elimina un nodo.

---

### 🎮 Progreso de Usuario
- `GET /api/stories/{story_id}/start/` — Devuelve el nodo inicial de la historia.
- `POST /api/stories/{story_id}/progress/` — Avanza al siguiente nodo según la elección.
  - Body: `{ "current_node_id": 7, "choice": "A" }`

---

### 💾 Guardado de Progreso
- `GET /api/progress/` — Ver el progreso actual del usuario en todas sus historias.
- `GET /api/progress/{story_id}/` — Progreso del usuario en una historia específica.
- `POST /api/progress/{story_id}/` — Guarda o actualiza el progreso.
- `DELETE /api/progress/{story_id}/` — Reinicia el progreso en esa historia.

---

### 🏁 Finales y Estadísticas
- `GET /api/stories/{story_id}/endings/` — Muestra todos los finales posibles (`is_ending=True`).
- `GET /api/stories/{story_id}/completed-by/` — Lista de usuarios que completaron la historia.

---

### 🌟 Extras (Opcional)
- `GET /api/stories/popular/` — Historias más populares (por completadas o votos).
- `POST /api/stories/{story_id}/vote/` — Vota una historia como favorita.

---

## 🧪 Autenticación
Algunos endpoints requieren autenticación (`IsAuthenticated`). Se recomienda usar token o basic auth en desarrollo.

---

## 🛠 Tecnologías
- Python 3
- Django
- Django REST Framework

---

## 📂 Estructura Sugerida
- `stories/` — App principal con modelos, vistas y urls.
- `users/` — (opcional) Para personalización de usuarios.

---

## 📝 Licencia
Este proyecto es de código abierto bajo la licencia MIT.
