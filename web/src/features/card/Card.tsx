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

    let suit_style = () => {

        switch(suit.name.toLowerCase()) {
            case Suit.Swords:
                return {boxShadow: '0 0 15px 7px #FF0000'}
            case Suit.Cups:
                return {boxShadow: '0 0 15px 7px #6495ED'}
            case Suit.Wands:
                return {boxShadow: '0 0 15px 7px #CD853F'}
            case Suit.Pentacles:
                return {boxShadow: '0 0 15px 7px #FFD700'}
            case Suit.Major:
                return {boxShadow: '0 0 20px 12px silver'}
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