import React from "react";
import {ComponentPreview, Previews} from "@react-buddy/ide-toolbox";
import {PaletteTree} from "./palette";
import Card from "../features/card/Card";
import {card} from "../interfacesa";
import Board from "../features/board/Board";


let caad: card = {
    id: 0,
    name: "Card",
    description: "Card",
    value: 5,
    state: true,
    suit: 'card',
    stats: {
        good: 1,
        luck: 2,
        order: 3,
        wild: true
    }

}

const ComponentPreviews = () => {
    return (
        <Previews palette={<PaletteTree/>}>
            <ComponentPreview path="/Card">
                <Card {...caad}/>
            </ComponentPreview>
            <ComponentPreview path="/Board">
                <Board/>
            </ComponentPreview>
        </Previews>
    );
};

export default ComponentPreviews;