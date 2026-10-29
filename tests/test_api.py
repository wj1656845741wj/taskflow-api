def test_register_and_login(client):
    # 测试注册
    response = client.post(
        "/auth/register",
        json={"username": "testuser", "email": "test@example.com", "password": "password123"}
    )
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"

    # 测试登录
    response = client.post(
        "/auth/login",
        data={"username": "testuser", "password": "password123"}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()


def test_create_task_without_auth(client):
    # 测试未登录时创建任务，应该返回 401
    response = client.post("/tasks/", json={"title": "Test Task"})
    assert response.status_code == 401


def test_create_and_get_task(client):
    # 注册并登录获取 Token (注意密码长度至少6位)
    client.post("/auth/register", json={"username": "user1", "email": "u1@example.com", "password": "password123"})
    login_res = client.post("/auth/login", data={"username": "user1", "password": "password123"})
    token = login_res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # 创建任务
    response = client.post(
        "/tasks/",
        json={"title": "My Task", "priority": "high"},
        headers=headers
    )
    assert response.status_code == 200
    task_id = response.json()["id"]

    # 获取任务
    response = client.get("/tasks/", headers=headers)
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["title"] == "My Task"