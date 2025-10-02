# Система версионирования (Semantic Versioning)

## Формат: `vMAJOR.MINOR.PATCH`

```
v1.5.3
│ │ │
│ │ └─ PATCH: Багфиксы, hotfix (1.5.0 → 1.5.1)
│ └─── MINOR: Новые фичи (1.4.0 → 1.5.0)
└───── MAJOR: Breaking changes (1.5.0 → 2.0.0)
```

## Примеры:

- `v1.5.0` → Добавили push-уведомления (новая фича)
- `v1.5.1` → Исправили баг с iOS push (hotfix)
- `v2.0.0` → Изменили структуру API (breaking change)
