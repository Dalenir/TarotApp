import {Navigate, useLocation} from "react-router-dom";
import {Button, Container, Form, Row} from "react-bootstrap";
import './Login.css';
import axios from "axios";
import React, {useState} from "react";

export default function Login() {
    const [name, setName] = useState("");
    const [password, setPassword] = useState("");
    const [redirect, setRedirect] = useState<JSX.Element | null>(null);


    function handleSubmit(event: React.FormEvent) {

        event.preventDefault();
        console.log(name, password)

        let formdata = new FormData();
        formdata.append("username", name);
        formdata.append("password", password);

        axios.post(`${import.meta.env.VITE_API_ROOT}/auth_token`, formdata, { withCredentials: true, })
            .then(res => {
                if (res.status === 200) {
                    console.log(res.data);
                    setRedirect(<Navigate to='/profile' state ={{from : location}}/>);
                }
            })

    }


    return (
        <>
            {redirect}
            <Container fluid className="align-items-center vh-100 d-flex justify-content-center">
                <Row className="login-container">
                    <h3 className='text-center mb-3'>Welcome to the</h3>
                    <h1 className='text-center mb-4 ttle'>Tarot Nevercode</h1>
                    <Form onSubmit={handleSubmit}>
                        <Form.Group className="mb-3" controlId="formBasicEmail">
                            <Form.Control
                                type="Username" size="lg" placeholder="Username"
                                value={name}
                                onChange={(e) => setName(e.target.value)} />
                        </Form.Group>

                        <Form.Group className="mb-3"  controlId="formBasicPassword">
                            <Form.Control
                                size="lg" type="password" placeholder="Password"
                                value={password}
                                onChange={(e) => setPassword(e.target.value)} />
                        </Form.Group>
                        <div className='d-flex justify-content-around'>
                            <Button variant="primary" size="lg" type="submit" className='log-button'>
                                Login
                            </Button>
                            <Button variant="outline-secondary" size="lg" type="button" className='log-button'
                                    href="/register">
                                Register
                            </Button>
                        </div>
                    </Form>
                </Row>
            </Container>
        </>
    );
}