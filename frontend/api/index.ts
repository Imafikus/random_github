import axios from 'axios';

interface GetCommentResponse {
  content: string
  url: string
}

export const getComment = async (): Promise<GetCommentResponse> => {
  const res = await axios.get(`${process.env.NEXT_PUBLIC_BACKEND_URL}/comment`);
  const data = res.data as GetCommentResponse;
  return data
}
