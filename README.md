# FastAPI Vite React
A barebones repo that can make it easier to develop and deploy a full-stack app using React and FastAPI.

## Built on:
- **FastAPI**: *Fast, simple, and has a modern design.*
- **Vite React `react-swc-ts`** : *Greatly simplifies the development process. Outstanding HMR support.*
- **MongoDB**: *Not just reliable and fast, but offer the ability to easily create distributed databases.*
- **Docker**: *Fundamental tool in modern development.*

## Includes:
- **React Buddy**: *I just love this Webstorm plugin! Will make it optional later.*


## Easy start:
1) Update all node packages:
    ```sh
    pushd web && bash enviroment_update.sh && popd 
    ```
2) Copy .env file from example:
   ```sh
   cp Deploy/.env.example Deploy/.env
   ```

3) Build dev images:
   ```sh
   docker compose -f Deploy/dev_compose.yml build
   ```

4) Start your app in dev mode
   ```sh
   docker compose -f Deploy/dev_compose.yml up
   ```

5) When you ready to ship, build and start it for production:
   ```sh
   docker compose -f Deploy/main_compose.yml build && docker compose -f Deploy/main_compose.yml up
   ```

---

- Make sure set API folder as source in Pycharm project
- Enviromental variables: Deploy/.env
- Logs: /logs

---

## Enviromental variables
**Deploy/.env**

| Variable             | Description                                                                                                             | Default         |
|----------------------|-------------------------------------------------------------------------------------------------------------------------|-----------------|
| API_PORT             | Port number <br/> *`INT`*                                                                                               | `8008 `         |
| DEBUG_MODE           | Debyg mode for development. More logs, autoreload from disk. <br/> *`String`* : `'True'/'False`                         | `True`          |
| COMPOSE_PROJECT_NAME | Name of compose group in docker listing. <br/>*`Строка`*                                                                | `ltl_fullstack` |
| DOCKER               | Launch method. Set on "Docker" for launch in container. Setting DEBUG_MODE on False. <br/> *`String`* : `'True'/'False` | `'True'`        |


---



### Usefull commands:

**Full API tests**: 
```sh 
docker compose -f Deploy/main_compose.yml run --rm ltl_api /bin/sh tests/all_tests_comm.sh
```


### Planned functionality:

1. Clearer API modes and variables.
2. Simplified QA.
   1. API unittests libraries to separate step in dockerfile.
   2. Container for backend and frontend QA tests .
3. One command project start.
4. More options for project creation.