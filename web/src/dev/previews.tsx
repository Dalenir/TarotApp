import React from "react";
import {ComponentPreview, Previews} from "@react-buddy/ide-toolbox";
import {PaletteTree} from "./palette";
import Card from "../features/card/Card";
import {card, suit} from "../interfacesa";
import Board from "../features/board/Board";


let card: card = {
    id: 0,
    name: "Card",
    description: "Card",
    value: 5,
    state: true,
    suit: {
        name: 'Swords',
        description: 'Test'},
    stats: {
        good: 1,
        luck: 2,
        order: 3,
        wild: true
    },
    size: { width: "13vh", height: "20vh" },
    visual_value: 'XVIII'
}

const ComponentPreviews = () => {
    const FlippyFlip =  () => {
        console.log("flip")
    }

    return (
        <Previews palette={<PaletteTree/>}>
            <ComponentPreview path="/Card">
                <Card {...card}
                      is_flipped={false}
                      flip_handle={FlippyFlip}/>
            </ComponentPreview>
            <ComponentPreview path="/Board">
                <Board/>
            </ComponentPreview>
        </Previews>
    );
};

export default ComponentPreviews;