export interface card {
    id: number,
    value: number,
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
    card: card
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