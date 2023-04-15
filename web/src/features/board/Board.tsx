import React, {useEffect, useState} from "react";
import axios from "axios";
import './Board.css'
import './buttons.css'
import Card from "../card/Card";
import {nanoid} from "nanoid";

interface mousePosInt {
    x: number
    y: number
}


export default function Board() {
    const [mousePos, setMousePos] = useState<mousePosInt>({x:0,y:0});
    const [cards, setCards] = useState<Array<JSX.Element>>([]);
    const [upd, setUpd] = useState<boolean>(true);


    useEffect(() => {
        const handleMouseMove = (event:React.MouseEvent) => {
            setMousePos({ x: event.clientX, y: event.clientY });
        };

        window.addEventListener('mousemove', handleMouseMove as any);

        return () => {
            // @ts-ignore
            window.removeEventListener(
                'mousemove',
                handleMouseMove as any
            );
        };
    }, []);

    function randCard () {
        return Math.floor(Math.random() * 21)
    }

    function allNewCards () {
        let doned:Array<number> = []
        let array = []
        for (let i=0; i<11; i++) {
            let x = randCard()
            while (doned.some(v => v === x)) {
                x = randCard()
            }
            doned.push(x)
            array.push(<div className="field" id={`field-${i}`}><Card number={x} is_preview={false} field={i} key={nanoid(5)}/></div>)

        }
        console.log('array', array)
        return array
    }


    useEffect(() => {
        setCards(allNewCards())
    }, [upd]);


    // @ts-ignore
    return(
        <div id="board">
            {cards}
            <button className="btn-68" onClick={() => {
                setUpd(!upd)
            }}>Gaze</button>
            <div id='textarea'></div>
        </div>
    )
}