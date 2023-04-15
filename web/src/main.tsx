import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import "./index.css";
import {DevSupport} from "@react-buddy/ide-toolbox";
import {ComponentPreviews, useInitial} from "./dev";
import Field from "./features/card/Field";
import Board from "./features/board/Board";

ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(
    <React.StrictMode>
        <DevSupport ComponentPreviews={ComponentPreviews}
                    useInitialHook={useInitial}
        >
            <Board/>
        </DevSupport>
    </React.StrictMode>,
);
