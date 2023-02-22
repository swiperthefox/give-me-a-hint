type CellType = "md" | "img" | "latex" | "asciimath"

export interface Cell {
    id: number,
    htmlContent: string,
    originalContent: string,
    type: CellType,
    next: Cell
}

export interface BookInfo {
    id: number,
    title: string,
    description: string,
    cover: string,
    lastUpdate: Date,
    createTime: Date
}

export interface Book {
    root: Cell,
    lastUpdate: Date
}

type ChangeType = "update" | "delete" | "new"

export interface ChangeDefinition {
    cell: Cell,
    type: ChangeType
}
