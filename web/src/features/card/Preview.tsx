import React from "react";
import Card from "./Card";
import './Preview.css'


interface PreviewProps {
    field?: number
    card_number: number
}

export default function Preview({ field, card_number }: PreviewProps) {

    return (
        <div className='prev-container'>
            <Card number={card_number} is_preview={true} field={field}/>
            <div className='prev-text'>
                <div className='text-pf'><p>Card number: {card_number}</p></div>
                <div className='text-pf'><p>Field number: {field}</p></div>
            </div>
        </div>
    )
}