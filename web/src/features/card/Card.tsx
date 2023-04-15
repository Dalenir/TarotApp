import React, {useEffect, useRef, useState} from "react";
import './Card.css'
import ReactCardFlip from 'react-card-flip';
import {unstable_batchedUpdates} from "react-dom";
import Preview from "./Preview";

interface CardProps {
    field?: number
    number: number
    is_preview: boolean
}

export default function Card({ field, number, is_preview}: CardProps) {
    const [preview, setPreview] = useState<JSX.Element>();
    const [isFlipped, setIsFlipped] = useState(!is_preview );
    const [bah_field, setBah_field] = useState(field);


    let makePrewiew = (card_number: number, event: React.MouseEvent, from_card_flip: boolean) => {
        if (isFlipped && !from_card_flip) {
            return
        }

        let rect = event.currentTarget.getBoundingClientRect();
        setPreview(
            <div
                className="card-prev visible"
                style={{
                    left: `${event.clientX - rect.left}px`,
                    top: `${event.clientY - rect.top}px`,
                    transform: event.clientY> window.innerHeight/2 ? "translate(0, -125%)" : "translate(0, -25%)"
                }}
            ><Preview card_number={card_number} field={field} />
            </div>)
    }

    function killPreview() {
        setPreview(undefined)
    }

    function FlippyFlip(event:React.MouseEvent) {
        if (isFlipped) {
            makePrewiew(number, event, true)
        } else {
            killPreview()
        }
        setIsFlipped((old_flipped) => !old_flipped)
    }

    const card_size = {
        height: !is_preview ? "20vh" : "40vh",
        width: !is_preview ? "13vh" : "26vh",
        zIndex: !is_preview ? 1 : 99,
        borderRadius: '10px'

    }

    const Is2BakaField: boolean = (field === 2) && !is_preview

    return(
         <div
             onMouseEnter={(event) => {!is_preview ? makePrewiew(number, event, false) : undefined}}
             onMouseLeave={killPreview}
             style={{
                 display: "flex",
                 justifyContent: "center",
                 alignItems: 'center',
                 height: Is2BakaField ? card_size.width : undefined,
                 width: Is2BakaField ? card_size.height : undefined,
         }}
         >
             <div className={ Is2BakaField ? "BakaField" : undefined}>
                 <ReactCardFlip isFlipped={isFlipped}>
                         <img
                             src={`${import.meta.env.VITE_API_ROOT}/card/${number}`}
                             style={card_size}
                             alt='Bah no image'
                             key='front'
                             onClick={!is_preview ? FlippyFlip : undefined}
                         />
                        <img src={`${import.meta.env.VITE_API_ROOT}/card/-1`} alt='bah no cover'
                             // className={`card-back ${Is2BakaField ? "BakaField" : undefined}`}
                             key='back'
                             onClick={FlippyFlip}
                             style={card_size}
                        />
                 </ReactCardFlip>
             </div>
             {preview && preview}
             <p>{bah_field}</p>
         </div>
    )
}