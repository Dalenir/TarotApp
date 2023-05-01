import {card} from "../../interfacesa";
import React from "react";
import ReactCardFlip from "react-card-flip";
import './Card.css'
import {SuitStyle} from "./suit_styles";


interface CardElementInteface extends card {
    is_flipped: boolean,
    flip_handle: any,
    size: {width: string, height: string}
}


export default function Card({ is_flipped, flip_handle, size, id, suit}:CardElementInteface) {

    let suit_style = SuitStyle[suit.name.toLowerCase() as keyof typeof SuitStyle]
    console.log(suit_style)


    return (
        <ReactCardFlip isFlipped={is_flipped} containerStyle={{...size}}>
            <img
                src={`${import.meta.env.VITE_API_ROOT}/card/${id}`}
                className='card'
                alt='Bah no image'
                key='front'
                onClick={() => flip_handle()}
                style={{...size, boxShadow: `0 0 15px 7px ${suit_style.main_color}`, borderRadius: '10px'}}
            />
            <img src={`${import.meta.env.VITE_API_ROOT}/card/-1`} alt='bah no cover'
                 key='back'
                 onClick={flip_handle}
                 className='card'
                 style={{...size, borderRadius: '10px'}}
            />
        </ReactCardFlip>
    )
}