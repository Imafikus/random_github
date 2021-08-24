import axios from 'axios';

interface GetCommentResponse {
  comment: string
}

export const getComment = async (): Promise<string> => {
  const res = await axios.get(`${process.env.NEXT_PUBLIC_BACKEND_URL}/comment`);
  const data = res.data as GetCommentResponse;
  return data.comment;
}
