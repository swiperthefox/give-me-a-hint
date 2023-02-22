export interface SuccessResponse<T> {
    success: true,
    data: T
}

export interface FailureResponse<T> {
    success: false,
    error: String
}

export type Response<T> = SuccessResponse<T> | FailureResponse<T>a

export interface NewBookInfo {
    title: String,
    cover: String,
    description: String
}