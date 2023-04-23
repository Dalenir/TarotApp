import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import {DevSupport} from "@react-buddy/ide-toolbox";
import {ComponentPreviews, useInitial} from "./dev";
import App from "./App";
import {BrowserRouter} from "react-router-dom";
import {CookiesProvider} from "react-cookie";
import './index.css'


ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(
    <BrowserRouter>
        <CookiesProvider>
            <DevSupport ComponentPreviews={ComponentPreviews}
                        useInitialHook={useInitial}
            >
                <App />
            </DevSupport>
        </CookiesProvider>
    </BrowserRouter>
);
