import {Routes, Route, Navigate, useNavigate} from "react-router-dom";
import 'bootstrap/dist/css/bootstrap.min.css';
import Login from "./features/auth/Login";
import Profile from "./features/auth/Profile";
import {Cookies} from "react-cookie";
import {RequireToken} from "./features/auth/auth";
import React, {useState} from "react";
import User_int from "./interfaces/user_int";
import { redirect } from "react-router-dom";
import Registration from "./features/auth/Registration";
import Board from "./features/board/Board";
import './App.css';

console.log(import.meta.env);
console.log(import.meta.env.PROD)

function App() {

    const [user, setUser] = useState<User_int|undefined>(undefined);
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
                <Route path="/register" element ={ <Registration /> } />
                <Route path="*" element={<Navigate to="/"/>}/>
            </Routes>
        </div>
    )
}

export default App
