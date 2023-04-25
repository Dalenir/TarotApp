import React, {FormEventHandler, useEffect, useState} from "react";
import {Button, Container, Form, Row} from "react-bootstrap";
import './Registration.css'
import axios from "axios";


interface RegistrationData {
    username: string,
    password: string,
    secpassword: string,
    email: string,
    code?: string
}

interface DisabledForms {
    formBasicUsername: boolean,
    formBasicEmail: boolean,
    formBasicPassword: boolean,
    formSecondPassword: boolean,
    formCheckCode: boolean
}

let startdisabledForms: DisabledForms = {
    formBasicUsername: false,
    formBasicEmail: false,
    formBasicPassword: false,
    formSecondPassword: false,
    formCheckCode: false
}


export default function Registration(): JSX.Element {

    const [validated_data, setValidatedData] = useState<RegistrationData|undefined>(undefined);
    const [disabledForms, setDisabledForms] = useState<DisabledForms>(startdisabledForms);


    const [codeFormVisible, setCodeFormVisible] = useState<boolean>();
    const handleVerification = (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        const form = event.currentTarget;
        if (!form.checkValidity()) {
            event.stopPropagation();
        }

        const {elements} = form
        const data = {
            username: (elements.namedItem("formBasicUsername") as HTMLInputElement).value,
            email: (elements.namedItem("formBasicEmail") as HTMLInputElement).value,
            password: (elements.namedItem("formBasicPassword") as HTMLTextAreaElement).value,
            secpassword: (elements.namedItem("formSecondPassword") as HTMLSelectElement).value,
        };

        if (data?.password !== data?.secpassword) {
            alert('Passwords are not equal!')
            return
        }
        console.log('1')

        let formdata = new FormData();
        formdata.append("email", data.email);
        axios.post(`${import.meta.env.VITE_API_ROOT}/security/new_user_reg`, formdata)
            .then(res => {
            console.log(res.data)
        })
        setValidatedData(data);
        setDisabledForms((old) => {
            let new_o: DisabledForms = {...old}
            Object.keys({...old}).forEach(function (key) {
                new_o[key as keyof DisabledForms] = true
            })
            return new_o
        })
    };

    const handleRegistration = (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        const form = event.currentTarget;
        const {elements} = form
        const data = {
            username: (elements.namedItem("formBasicUsername") as HTMLInputElement).value,
            email: (elements.namedItem("formBasicEmail") as HTMLInputElement).value,
            password: (elements.namedItem("formBasicPassword") as HTMLTextAreaElement).value,
            secpassword: (elements.namedItem("formSecondPassword") as HTMLSelectElement).value,
            code: (elements.namedItem("formCheckCode") as HTMLSelectElement).value,
        };
        let formdata = new FormData();
        for (let dataKey in data) {
            formdata.append(dataKey, data[dataKey as keyof RegistrationData]);
        }
        // TODO: 1) make a lot of checks and make a valid redirect
        axios.post(`${import.meta.env.VITE_API_ROOT}/security/email_code_verify`, formdata)
            .then(res => {res.status === 200 && res.data.success && alert('Registration is successful!')})
            .catch(err => {
                console.log(err)
                alert('Registration is failed!')
    })
    }

    function NotReallyDisabled (event: React.MouseEvent) {
        let idd = (event.target as HTMLInputElement).id
        setDisabledForms((old) => {
            return {...old,
                    [idd]: false
            }
        })
    }

    function EmailChange (event: React.FormEvent<HTMLElement>) {
        setValidatedData(undefined);
    }


    return (
        <Container fluid className="align-items-center vh-100 d-flex justify-content-center flex-column gap-md-3">
            <Row><h1 className='text-center mb-md-3'>Registration</h1></Row>
            <Row className="login-container">
                <Form onSubmit={!validated_data?handleVerification:handleRegistration}>
                    <div className='d-flex justify-content-center gap-2 mx-2 mb-2'>
                        <Form.Group controlId="formBasicUsername" onClick={NotReallyDisabled}>
                            <Form.Control
                                type="text" size="lg" placeholder="Username"  disabled={disabledForms.formBasicUsername}
                            />
                        </Form.Group>
                        <Form.Group controlId="formBasicEmail" onChange={EmailChange} onClick={NotReallyDisabled}>
                            <Form.Control
                                type="email" size="lg" placeholder="E-mail"  disabled={disabledForms.formBasicEmail}
                            />
                        </Form.Group>
                    </div>
                    <Form.Group className="mx-2 mb-2"  controlId="formBasicPassword" onClick={NotReallyDisabled}>
                        <Form.Control
                            size="lg" type="password" placeholder="Password"  disabled={disabledForms.formBasicPassword}
                        />
                    </Form.Group>
                    <Form.Group className="m-2"  controlId="formSecondPassword" onClick={NotReallyDisabled}>
                        <Form.Control
                            size="lg" type="password" placeholder="Repeat Password"  disabled={disabledForms.formSecondPassword}
                        />
                    </Form.Group>
                    <Form.Group className={!validated_data?"d-none":"m-2"}  controlId="formCheckCode">
                        <Form.Control
                            size="lg" type="text" className='text-center' placeholder="Code from Email"
                        />
                    </Form.Group>
                    <div className='mx-2'>
                        <Button
                                variant="primary"
                                size="lg"
                                type="submit"
                                id={'big-submit-button'}>
                            {validated_data?'Verify code':'Get verification code'}
                        </Button>
                    </div>
                </Form>
            </Row>
        </Container>
    )
}
