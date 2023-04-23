import {Routes, Route, Navigate, useNavigate} from "react-router-dom";
import 'bootstrap/dist/css/bootstrap.min.css';
import Login from "./features/auth/Login";
import Profile from "./features/auth/Profile";
import {Cookies} from "react-cookie";
import {RequireToken} from "./features/auth/auth";
import React, {useState} from "react";
import User from "./interfaces/User";
import { redirect } from "react-router-dom";

console.log(import.meta.env);
console.log(import.meta.env.PROD)

function App() {

    const [user, setUser] = useState<User|undefined>(undefined);
    const nav = useNavigate();
    const cookies = new Cookies();

    console.log('app level', user)

    function LogOut(){
        cookies.remove("access_token", {path: '/'});
        cookies.remove("csrf_token", {path: '/'});
        setUser(undefined);
        console.log('logout')
        nav('/')
    }

    
    return (
        <div className ="App">
            <Routes>
                <Route path="/" element = {<Login/>}/>
                <Route path="/profile" element = {
                    <RequireToken user_set={setUser}>
                        <Profile user={user} handle_logout={LogOut} />
                    </RequireToken>
                }/>
            </Routes>
        </div>
    )
}

export default App
