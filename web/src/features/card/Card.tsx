import {card} from "../../interfacesa";
import React from "react";
import ReactCardFlip from "react-card-flip";
import './Card.css'


interface CardElementInteface extends card {
    is_flipped: boolean,
    flip_handle: any,
    size: {width: string, height: string}
}


enum Suit {
    Swords = 'swords',
    Wands = 'wands',
    Cups = 'cups',
    Pentacles = 'pentacles',
    Major = 'major arcana'
}


export default function Card({ is_flipped, flip_handle, size, id, suit}:CardElementInteface) {


    console.log(suit)
    let suit_style = () => {

        switch(suit.name.toLowerCase()) {
            case Suit.Swords:
                return {outline: '5px inset crimson'}
            case Suit.Cups:
                return {outline: '5px inset blue'}
            case Suit.Wands:
                return {outline: '5px inset firebrick'}
            case Suit.Pentacles:
                return {outline: '5px inset gold'}
            case Suit.Major:
                return {outline: '8px inset silver'}
        }
    }

    return (
        <ReactCardFlip isFlipped={is_flipped} containerStyle={{...size}}>
            <img
                src={`${import.meta.env.VITE_API_ROOT}/card/${id}`}
                className='card'
                alt='Bah no image'
                key='front'
                onClick={() => flip_handle()}
                style={{...size, ...suit_style(), borderRadius: '10px'}}
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