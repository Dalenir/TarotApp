import React, {useEffect, useState} from "react";
import axios from "axios";
import './Board.css'
import './buttons.css'
import type {board} from "../../interfacesa"
import Field from "../card/Field";
import {nanoid} from "nanoid";
import User from "../../interfaces/User";

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

    useEffect(() => { document.body.style.backgroundColor = '#05072c' }, [])

    function allNewCards () {
        axios.get(`${import.meta.env.VITE_API_ROOT}/refresh_board`)
            .then(r => {
                if (r.status === 200) {
                    const new_board: board = JSON.parse(r.data)
                    setCards(new_board.fields.map((field) =>
                        <Field {...field} key={nanoid(5)}/>
                    ))
                }
            })
    }


    useEffect(() => {
        allNewCards()
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