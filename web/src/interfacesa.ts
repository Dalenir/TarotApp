export interface card {
    id: number,
    value: number,
    visual_value: string,
    name: string,
    suit: suit,
    state: boolean,
    stats: stats,
    description: string,
    size: { width: string, height: string }
}

export interface field {
    number: number,
    description: string,
    name: string,
    card: card,
}

export interface board {
    fields: Array<field>
}

export interface stats {
    good: number
    luck: number
    order: number
    wild: boolean
}

export interface suit {
    name: string
    description: string
}