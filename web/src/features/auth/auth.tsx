import { useLocation,Navigate } from "react-router-dom"
import {Cookies} from "react-cookie";
import React, {JSXElementConstructor, ReactElement, useEffect, useState} from "react";
import axios from "axios";

export function RequireToken({ children, user_set } : {
    children: ReactElement,
    user_set: React.Dispatch<any>
}) {

    const [redirect, setRedirect] = useState<ReactElement|null>(null);
    let location = useLocation()

    useEffect(() => {
        const csrf = new Cookies().get('csrf_token')
        let bodyFormData = new FormData();
        bodyFormData.append('csrf_token', csrf);
        axios.post(`${import.meta.env.VITE_API_ROOT}/user_profile`, bodyFormData , { withCredentials: true})
            .then(r => {
                if (r.status === 200) {
                    let enchantChild: ReactElement = React.cloneElement(children, {user:
                            {name: r.data.sub, payer: r.data.payer}
                    })
                    setRedirect(enchantChild)
                    user_set((prev: object) =>  {
                        return {name: r.data.sub}
                    } )
                } else {
                    setRedirect(children)
                }}).catch(function (error) {
                setRedirect(<Navigate to='/' state ={{from : location}}/>);
        })
    }, []);

    return redirect;

}