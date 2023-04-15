import React from "react";
import {ComponentPreview, Previews} from "@react-buddy/ide-toolbox";
import {PaletteTree} from "./palette";
import App from "../App";
import Card from "../features/card/Card";
import Board from "../features/board/Board";
import Preview from "../features/card/Preview";

const ComponentPreviews = () => {
    // @ts-ignore
    return (
        <Previews palette={<PaletteTree/>}>
            <ComponentPreview path="/App">
                <App/>
            </ComponentPreview>
            <ComponentPreview path="/Card">
                <Card number={0} field={0} is_preview={false}/>
            </ComponentPreview>
            <ComponentPreview path="/Board">
                <Board/>
            </ComponentPreview>
            <ComponentPreview path="/Preview">
                <Preview card_number={0} field={0}/>
            </ComponentPreview>
        </Previews>
    );
};

export default ComponentPreviews;