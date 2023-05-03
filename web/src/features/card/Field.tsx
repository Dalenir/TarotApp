import React, {useEffect, useState} from "react";
import './Field.css'
import Preview from "./Preview";
import Card from "./Card";
import {field} from "../../interfaces/field_int";


interface FieldElementInterface extends field {
    update_outer_texts: Function
}



export default function Field({number, description, card, name, update_outer_texts}: FieldElementInterface) {
    const [preview, setPreview] = useState<JSX.Element>();
    const [isFlipped, setIsFlipped] = useState(true);

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
            ><Preview {...{number, description, card, field_size, name}} />
            </div>)
    }

    function killPreview() {
        setPreview(undefined)
    }

    const field_size = {
        height: "20vh",
        width: "13vh",
    }

    function FlippyFlip(event:React.MouseEvent) {
        if (isFlipped) {
            makePrewiew(number, event, true)
        } else {
            killPreview()
        }
        setIsFlipped((old_flipped) => !old_flipped)
        update_outer_texts({number, description, card, name})
    }

    return(
        <div className='field' id={`field-${number}`}>
         <div
             onMouseEnter={(event) => {makePrewiew(number, event, false)}}
             onMouseLeave={killPreview}
             style={{
                 display: "flex",
                 justifyContent: "center",
                 alignItems: 'center',
                 height: number === 2 ? field_size.width : field_size.height,
                 width: number === 2 ? field_size.height : field_size.width,
         }}
         >
             <div style={{transform: number === 2 ? 'rotate(-90deg)' : !card.state ? 'rotate(-180deg)': undefined}}>
                 <Card {...card}
                       is_flipped={isFlipped}
                       flip_handle={FlippyFlip}
                       size={field_size}
                 />
             </div>
             {preview && preview}
         </div>
        </div>
    )
}