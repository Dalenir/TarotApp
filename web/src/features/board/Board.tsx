import React, {useEffect, useState} from "react";
import axios from "axios";
import './Board.css'
import './buttons.css'
import type {board, field} from "../../interfacesa"
import Field from "../card/Field";
import {nanoid} from "nanoid";

interface mousePosInt {
    x: number
    y: number
}



export default function Board() {
    const [mousePos, setMousePos] = useState<mousePosInt>({x:0,y:0});
    const [cards, setCards] = useState<Array<JSX.Element>>([]);
    const [fieldData, setFieldData] = useState<Array<field>>([]);
    const [upd, setUpd] = useState<boolean>(true);
    const [resultTexts, setResultTexts] = useState<Array<field>>([]);

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

    useEffect(() => {
        document.body.style.backgroundColor = '#05072c'
        return () => { document.body.style.backgroundColor = "#fffbf0"}
    }, [])

    function updateResultTexts(field: field) {
        setResultTexts(old_texts => {
            console.log(fieldData)
            if (old_texts.length > 0) {
                console.log('Not empty array')
                if (old_texts.filter(old_field => old_field.number === field.number).length > 0) {
                    // console.log('Field in array ' +  field.number)
                    return old_texts.filter(old_field => old_field.number !== field.number)
                } else {
                    // console.log('Field not in array ' +  field.number)
                    return old_texts.concat(field)
                        .sort((a,b) => a.number - b.number)
                }
            } else {
                // console.log('Empty array')
                return [field]
            }
        })
    }


    function allNewCards () {
        axios.get(`${import.meta.env.VITE_API_ROOT}/refresh_board`)
            .then(r => {
                if (r.status === 200) {
                    const new_board: board = JSON.parse(r.data)
                    console.log(new_board.fields)
                    setResultTexts([])
                    setCards(new_board.fields.map((field) =>
                        <Field {...field} update_outer_texts={updateResultTexts} key={nanoid(5)}/>
                    ))
                    setFieldData(new_board.fields)
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
            <div id='textarea'>
                {resultTexts && resultTexts.map(field =>
                    <div className='textarea-field' key={field.number}>
                        <p><b>{field.number}. {field.name}: </b>{field.card.description}</p>
                    </div>
                )}
            </div>
        </div>
    )
}