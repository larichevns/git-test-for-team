```
main (production, всегда стабильная)
│
├── v1.4.0, v1.5.0, v1.5.1 (теги версий)
│
├── develop (staging, интеграция фич)
│   │
│   ├── feature/* (новые фичи)
│   │   ├── feature/TASK-123-push-notifications-api
│   │   ├── feature/TASK-124-user-profile-edit
│   │   └── feature/TASK-125-export-csv
│   │
│   └── fix/* (исправление багов в develop)
│       ├── fix/BUG-45-ios-push-notifications
│       └── fix/BUG-46-form-validation
│
└── hotfix/* (критические баги в production)
    └── hotfix/payment-processing-error
```

## Назначение веток:

| Ветка | Назначение | Живёт | От кого | Мерджится в |
|-------|------------|-------|---------|-------------|
| `main` | Production, только стабильный код | Постоянно | - | - |
| `develop` | Staging, интеграция всех фич | Постоянно | `main` | `main` |
| `feature/*` | Разработка новых фич | До мерджа | `develop` | `develop` |
| `fix/*` | Исправление багов после тестирования | До мерджа | `develop` | `develop` |
| `hotfix/*` | Критические баги в production | До мерджа | `main` | `main` + `develop` |
