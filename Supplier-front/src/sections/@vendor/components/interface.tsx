export interface TextInputProps {
  label: string;
  name: string;
  value: string;
  fullWidth?: boolean;
  handleChange: (event: React.ChangeEvent<HTMLInputElement>) => void;
  handleBlur: (event: React.FocusEvent<HTMLInputElement>) => void;
}

export interface TimeInputProps {
  label: string;
  name: string;
  value: string;
  fullWidth?: boolean;
  handleChange: (event: React.ChangeEvent<HTMLInputElement>) => void;
  handleBlur: (event: React.FocusEvent<HTMLInputElement>) => void;
}

export interface UrlInputProps {
  label: string;
  name: string;
  value: string;
  fullWidth?: boolean;
  onChange: (event: React.ChangeEvent<HTMLInputElement>) => void;
  onBlur: (event: React.FocusEvent<HTMLInputElement>) => void;
}
