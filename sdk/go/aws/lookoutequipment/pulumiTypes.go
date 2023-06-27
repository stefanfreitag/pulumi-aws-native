// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package lookoutequipment

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Specifies configuration information for the input data for the inference scheduler, including delimiter, format, and dataset location.
type DataInputConfigurationProperties struct {
	InferenceInputNameConfiguration *InferenceSchedulerInputNameConfiguration `pulumi:"inferenceInputNameConfiguration"`
	// Indicates the difference between your time zone and Greenwich Mean Time (GMT).
	InputTimeZoneOffset  *string                                `pulumi:"inputTimeZoneOffset"`
	S3InputConfiguration InferenceSchedulerS3InputConfiguration `pulumi:"s3InputConfiguration"`
}

// DataInputConfigurationPropertiesInput is an input type that accepts DataInputConfigurationPropertiesArgs and DataInputConfigurationPropertiesOutput values.
// You can construct a concrete instance of `DataInputConfigurationPropertiesInput` via:
//
//	DataInputConfigurationPropertiesArgs{...}
type DataInputConfigurationPropertiesInput interface {
	pulumi.Input

	ToDataInputConfigurationPropertiesOutput() DataInputConfigurationPropertiesOutput
	ToDataInputConfigurationPropertiesOutputWithContext(context.Context) DataInputConfigurationPropertiesOutput
}

// Specifies configuration information for the input data for the inference scheduler, including delimiter, format, and dataset location.
type DataInputConfigurationPropertiesArgs struct {
	InferenceInputNameConfiguration InferenceSchedulerInputNameConfigurationPtrInput `pulumi:"inferenceInputNameConfiguration"`
	// Indicates the difference between your time zone and Greenwich Mean Time (GMT).
	InputTimeZoneOffset  pulumi.StringPtrInput                       `pulumi:"inputTimeZoneOffset"`
	S3InputConfiguration InferenceSchedulerS3InputConfigurationInput `pulumi:"s3InputConfiguration"`
}

func (DataInputConfigurationPropertiesArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*DataInputConfigurationProperties)(nil)).Elem()
}

func (i DataInputConfigurationPropertiesArgs) ToDataInputConfigurationPropertiesOutput() DataInputConfigurationPropertiesOutput {
	return i.ToDataInputConfigurationPropertiesOutputWithContext(context.Background())
}

func (i DataInputConfigurationPropertiesArgs) ToDataInputConfigurationPropertiesOutputWithContext(ctx context.Context) DataInputConfigurationPropertiesOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DataInputConfigurationPropertiesOutput)
}

// Specifies configuration information for the input data for the inference scheduler, including delimiter, format, and dataset location.
type DataInputConfigurationPropertiesOutput struct{ *pulumi.OutputState }

func (DataInputConfigurationPropertiesOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*DataInputConfigurationProperties)(nil)).Elem()
}

func (o DataInputConfigurationPropertiesOutput) ToDataInputConfigurationPropertiesOutput() DataInputConfigurationPropertiesOutput {
	return o
}

func (o DataInputConfigurationPropertiesOutput) ToDataInputConfigurationPropertiesOutputWithContext(ctx context.Context) DataInputConfigurationPropertiesOutput {
	return o
}

func (o DataInputConfigurationPropertiesOutput) InferenceInputNameConfiguration() InferenceSchedulerInputNameConfigurationPtrOutput {
	return o.ApplyT(func(v DataInputConfigurationProperties) *InferenceSchedulerInputNameConfiguration {
		return v.InferenceInputNameConfiguration
	}).(InferenceSchedulerInputNameConfigurationPtrOutput)
}

// Indicates the difference between your time zone and Greenwich Mean Time (GMT).
func (o DataInputConfigurationPropertiesOutput) InputTimeZoneOffset() pulumi.StringPtrOutput {
	return o.ApplyT(func(v DataInputConfigurationProperties) *string { return v.InputTimeZoneOffset }).(pulumi.StringPtrOutput)
}

func (o DataInputConfigurationPropertiesOutput) S3InputConfiguration() InferenceSchedulerS3InputConfigurationOutput {
	return o.ApplyT(func(v DataInputConfigurationProperties) InferenceSchedulerS3InputConfiguration {
		return v.S3InputConfiguration
	}).(InferenceSchedulerS3InputConfigurationOutput)
}

type DataInputConfigurationPropertiesPtrOutput struct{ *pulumi.OutputState }

func (DataInputConfigurationPropertiesPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**DataInputConfigurationProperties)(nil)).Elem()
}

func (o DataInputConfigurationPropertiesPtrOutput) ToDataInputConfigurationPropertiesPtrOutput() DataInputConfigurationPropertiesPtrOutput {
	return o
}

func (o DataInputConfigurationPropertiesPtrOutput) ToDataInputConfigurationPropertiesPtrOutputWithContext(ctx context.Context) DataInputConfigurationPropertiesPtrOutput {
	return o
}

func (o DataInputConfigurationPropertiesPtrOutput) Elem() DataInputConfigurationPropertiesOutput {
	return o.ApplyT(func(v *DataInputConfigurationProperties) DataInputConfigurationProperties {
		if v != nil {
			return *v
		}
		var ret DataInputConfigurationProperties
		return ret
	}).(DataInputConfigurationPropertiesOutput)
}

func (o DataInputConfigurationPropertiesPtrOutput) InferenceInputNameConfiguration() InferenceSchedulerInputNameConfigurationPtrOutput {
	return o.ApplyT(func(v *DataInputConfigurationProperties) *InferenceSchedulerInputNameConfiguration {
		if v == nil {
			return nil
		}
		return v.InferenceInputNameConfiguration
	}).(InferenceSchedulerInputNameConfigurationPtrOutput)
}

// Indicates the difference between your time zone and Greenwich Mean Time (GMT).
func (o DataInputConfigurationPropertiesPtrOutput) InputTimeZoneOffset() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DataInputConfigurationProperties) *string {
		if v == nil {
			return nil
		}
		return v.InputTimeZoneOffset
	}).(pulumi.StringPtrOutput)
}

func (o DataInputConfigurationPropertiesPtrOutput) S3InputConfiguration() InferenceSchedulerS3InputConfigurationPtrOutput {
	return o.ApplyT(func(v *DataInputConfigurationProperties) *InferenceSchedulerS3InputConfiguration {
		if v == nil {
			return nil
		}
		return &v.S3InputConfiguration
	}).(InferenceSchedulerS3InputConfigurationPtrOutput)
}

// Specifies configuration information for the output results for the inference scheduler, including the S3 location for the output.
type DataOutputConfigurationProperties struct {
	// The ID number for the AWS KMS key used to encrypt the inference output.
	KmsKeyId              *string                                 `pulumi:"kmsKeyId"`
	S3OutputConfiguration InferenceSchedulerS3OutputConfiguration `pulumi:"s3OutputConfiguration"`
}

// DataOutputConfigurationPropertiesInput is an input type that accepts DataOutputConfigurationPropertiesArgs and DataOutputConfigurationPropertiesOutput values.
// You can construct a concrete instance of `DataOutputConfigurationPropertiesInput` via:
//
//	DataOutputConfigurationPropertiesArgs{...}
type DataOutputConfigurationPropertiesInput interface {
	pulumi.Input

	ToDataOutputConfigurationPropertiesOutput() DataOutputConfigurationPropertiesOutput
	ToDataOutputConfigurationPropertiesOutputWithContext(context.Context) DataOutputConfigurationPropertiesOutput
}

// Specifies configuration information for the output results for the inference scheduler, including the S3 location for the output.
type DataOutputConfigurationPropertiesArgs struct {
	// The ID number for the AWS KMS key used to encrypt the inference output.
	KmsKeyId              pulumi.StringPtrInput                        `pulumi:"kmsKeyId"`
	S3OutputConfiguration InferenceSchedulerS3OutputConfigurationInput `pulumi:"s3OutputConfiguration"`
}

func (DataOutputConfigurationPropertiesArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*DataOutputConfigurationProperties)(nil)).Elem()
}

func (i DataOutputConfigurationPropertiesArgs) ToDataOutputConfigurationPropertiesOutput() DataOutputConfigurationPropertiesOutput {
	return i.ToDataOutputConfigurationPropertiesOutputWithContext(context.Background())
}

func (i DataOutputConfigurationPropertiesArgs) ToDataOutputConfigurationPropertiesOutputWithContext(ctx context.Context) DataOutputConfigurationPropertiesOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DataOutputConfigurationPropertiesOutput)
}

// Specifies configuration information for the output results for the inference scheduler, including the S3 location for the output.
type DataOutputConfigurationPropertiesOutput struct{ *pulumi.OutputState }

func (DataOutputConfigurationPropertiesOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*DataOutputConfigurationProperties)(nil)).Elem()
}

func (o DataOutputConfigurationPropertiesOutput) ToDataOutputConfigurationPropertiesOutput() DataOutputConfigurationPropertiesOutput {
	return o
}

func (o DataOutputConfigurationPropertiesOutput) ToDataOutputConfigurationPropertiesOutputWithContext(ctx context.Context) DataOutputConfigurationPropertiesOutput {
	return o
}

// The ID number for the AWS KMS key used to encrypt the inference output.
func (o DataOutputConfigurationPropertiesOutput) KmsKeyId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v DataOutputConfigurationProperties) *string { return v.KmsKeyId }).(pulumi.StringPtrOutput)
}

func (o DataOutputConfigurationPropertiesOutput) S3OutputConfiguration() InferenceSchedulerS3OutputConfigurationOutput {
	return o.ApplyT(func(v DataOutputConfigurationProperties) InferenceSchedulerS3OutputConfiguration {
		return v.S3OutputConfiguration
	}).(InferenceSchedulerS3OutputConfigurationOutput)
}

type DataOutputConfigurationPropertiesPtrOutput struct{ *pulumi.OutputState }

func (DataOutputConfigurationPropertiesPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**DataOutputConfigurationProperties)(nil)).Elem()
}

func (o DataOutputConfigurationPropertiesPtrOutput) ToDataOutputConfigurationPropertiesPtrOutput() DataOutputConfigurationPropertiesPtrOutput {
	return o
}

func (o DataOutputConfigurationPropertiesPtrOutput) ToDataOutputConfigurationPropertiesPtrOutputWithContext(ctx context.Context) DataOutputConfigurationPropertiesPtrOutput {
	return o
}

func (o DataOutputConfigurationPropertiesPtrOutput) Elem() DataOutputConfigurationPropertiesOutput {
	return o.ApplyT(func(v *DataOutputConfigurationProperties) DataOutputConfigurationProperties {
		if v != nil {
			return *v
		}
		var ret DataOutputConfigurationProperties
		return ret
	}).(DataOutputConfigurationPropertiesOutput)
}

// The ID number for the AWS KMS key used to encrypt the inference output.
func (o DataOutputConfigurationPropertiesPtrOutput) KmsKeyId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DataOutputConfigurationProperties) *string {
		if v == nil {
			return nil
		}
		return v.KmsKeyId
	}).(pulumi.StringPtrOutput)
}

func (o DataOutputConfigurationPropertiesPtrOutput) S3OutputConfiguration() InferenceSchedulerS3OutputConfigurationPtrOutput {
	return o.ApplyT(func(v *DataOutputConfigurationProperties) *InferenceSchedulerS3OutputConfiguration {
		if v == nil {
			return nil
		}
		return &v.S3OutputConfiguration
	}).(InferenceSchedulerS3OutputConfigurationPtrOutput)
}

// Specifies configuration information for the input data for the inference, including timestamp format and delimiter.
type InferenceSchedulerInputNameConfiguration struct {
	// Indicates the delimiter character used between items in the data.
	ComponentTimestampDelimiter *string `pulumi:"componentTimestampDelimiter"`
	// The format of the timestamp, whether Epoch time, or standard, with or without hyphens (-).
	TimestampFormat *string `pulumi:"timestampFormat"`
}

// InferenceSchedulerInputNameConfigurationInput is an input type that accepts InferenceSchedulerInputNameConfigurationArgs and InferenceSchedulerInputNameConfigurationOutput values.
// You can construct a concrete instance of `InferenceSchedulerInputNameConfigurationInput` via:
//
//	InferenceSchedulerInputNameConfigurationArgs{...}
type InferenceSchedulerInputNameConfigurationInput interface {
	pulumi.Input

	ToInferenceSchedulerInputNameConfigurationOutput() InferenceSchedulerInputNameConfigurationOutput
	ToInferenceSchedulerInputNameConfigurationOutputWithContext(context.Context) InferenceSchedulerInputNameConfigurationOutput
}

// Specifies configuration information for the input data for the inference, including timestamp format and delimiter.
type InferenceSchedulerInputNameConfigurationArgs struct {
	// Indicates the delimiter character used between items in the data.
	ComponentTimestampDelimiter pulumi.StringPtrInput `pulumi:"componentTimestampDelimiter"`
	// The format of the timestamp, whether Epoch time, or standard, with or without hyphens (-).
	TimestampFormat pulumi.StringPtrInput `pulumi:"timestampFormat"`
}

func (InferenceSchedulerInputNameConfigurationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*InferenceSchedulerInputNameConfiguration)(nil)).Elem()
}

func (i InferenceSchedulerInputNameConfigurationArgs) ToInferenceSchedulerInputNameConfigurationOutput() InferenceSchedulerInputNameConfigurationOutput {
	return i.ToInferenceSchedulerInputNameConfigurationOutputWithContext(context.Background())
}

func (i InferenceSchedulerInputNameConfigurationArgs) ToInferenceSchedulerInputNameConfigurationOutputWithContext(ctx context.Context) InferenceSchedulerInputNameConfigurationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(InferenceSchedulerInputNameConfigurationOutput)
}

func (i InferenceSchedulerInputNameConfigurationArgs) ToInferenceSchedulerInputNameConfigurationPtrOutput() InferenceSchedulerInputNameConfigurationPtrOutput {
	return i.ToInferenceSchedulerInputNameConfigurationPtrOutputWithContext(context.Background())
}

func (i InferenceSchedulerInputNameConfigurationArgs) ToInferenceSchedulerInputNameConfigurationPtrOutputWithContext(ctx context.Context) InferenceSchedulerInputNameConfigurationPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(InferenceSchedulerInputNameConfigurationOutput).ToInferenceSchedulerInputNameConfigurationPtrOutputWithContext(ctx)
}

// InferenceSchedulerInputNameConfigurationPtrInput is an input type that accepts InferenceSchedulerInputNameConfigurationArgs, InferenceSchedulerInputNameConfigurationPtr and InferenceSchedulerInputNameConfigurationPtrOutput values.
// You can construct a concrete instance of `InferenceSchedulerInputNameConfigurationPtrInput` via:
//
//	        InferenceSchedulerInputNameConfigurationArgs{...}
//
//	or:
//
//	        nil
type InferenceSchedulerInputNameConfigurationPtrInput interface {
	pulumi.Input

	ToInferenceSchedulerInputNameConfigurationPtrOutput() InferenceSchedulerInputNameConfigurationPtrOutput
	ToInferenceSchedulerInputNameConfigurationPtrOutputWithContext(context.Context) InferenceSchedulerInputNameConfigurationPtrOutput
}

type inferenceSchedulerInputNameConfigurationPtrType InferenceSchedulerInputNameConfigurationArgs

func InferenceSchedulerInputNameConfigurationPtr(v *InferenceSchedulerInputNameConfigurationArgs) InferenceSchedulerInputNameConfigurationPtrInput {
	return (*inferenceSchedulerInputNameConfigurationPtrType)(v)
}

func (*inferenceSchedulerInputNameConfigurationPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**InferenceSchedulerInputNameConfiguration)(nil)).Elem()
}

func (i *inferenceSchedulerInputNameConfigurationPtrType) ToInferenceSchedulerInputNameConfigurationPtrOutput() InferenceSchedulerInputNameConfigurationPtrOutput {
	return i.ToInferenceSchedulerInputNameConfigurationPtrOutputWithContext(context.Background())
}

func (i *inferenceSchedulerInputNameConfigurationPtrType) ToInferenceSchedulerInputNameConfigurationPtrOutputWithContext(ctx context.Context) InferenceSchedulerInputNameConfigurationPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(InferenceSchedulerInputNameConfigurationPtrOutput)
}

// Specifies configuration information for the input data for the inference, including timestamp format and delimiter.
type InferenceSchedulerInputNameConfigurationOutput struct{ *pulumi.OutputState }

func (InferenceSchedulerInputNameConfigurationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*InferenceSchedulerInputNameConfiguration)(nil)).Elem()
}

func (o InferenceSchedulerInputNameConfigurationOutput) ToInferenceSchedulerInputNameConfigurationOutput() InferenceSchedulerInputNameConfigurationOutput {
	return o
}

func (o InferenceSchedulerInputNameConfigurationOutput) ToInferenceSchedulerInputNameConfigurationOutputWithContext(ctx context.Context) InferenceSchedulerInputNameConfigurationOutput {
	return o
}

func (o InferenceSchedulerInputNameConfigurationOutput) ToInferenceSchedulerInputNameConfigurationPtrOutput() InferenceSchedulerInputNameConfigurationPtrOutput {
	return o.ToInferenceSchedulerInputNameConfigurationPtrOutputWithContext(context.Background())
}

func (o InferenceSchedulerInputNameConfigurationOutput) ToInferenceSchedulerInputNameConfigurationPtrOutputWithContext(ctx context.Context) InferenceSchedulerInputNameConfigurationPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v InferenceSchedulerInputNameConfiguration) *InferenceSchedulerInputNameConfiguration {
		return &v
	}).(InferenceSchedulerInputNameConfigurationPtrOutput)
}

// Indicates the delimiter character used between items in the data.
func (o InferenceSchedulerInputNameConfigurationOutput) ComponentTimestampDelimiter() pulumi.StringPtrOutput {
	return o.ApplyT(func(v InferenceSchedulerInputNameConfiguration) *string { return v.ComponentTimestampDelimiter }).(pulumi.StringPtrOutput)
}

// The format of the timestamp, whether Epoch time, or standard, with or without hyphens (-).
func (o InferenceSchedulerInputNameConfigurationOutput) TimestampFormat() pulumi.StringPtrOutput {
	return o.ApplyT(func(v InferenceSchedulerInputNameConfiguration) *string { return v.TimestampFormat }).(pulumi.StringPtrOutput)
}

type InferenceSchedulerInputNameConfigurationPtrOutput struct{ *pulumi.OutputState }

func (InferenceSchedulerInputNameConfigurationPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**InferenceSchedulerInputNameConfiguration)(nil)).Elem()
}

func (o InferenceSchedulerInputNameConfigurationPtrOutput) ToInferenceSchedulerInputNameConfigurationPtrOutput() InferenceSchedulerInputNameConfigurationPtrOutput {
	return o
}

func (o InferenceSchedulerInputNameConfigurationPtrOutput) ToInferenceSchedulerInputNameConfigurationPtrOutputWithContext(ctx context.Context) InferenceSchedulerInputNameConfigurationPtrOutput {
	return o
}

func (o InferenceSchedulerInputNameConfigurationPtrOutput) Elem() InferenceSchedulerInputNameConfigurationOutput {
	return o.ApplyT(func(v *InferenceSchedulerInputNameConfiguration) InferenceSchedulerInputNameConfiguration {
		if v != nil {
			return *v
		}
		var ret InferenceSchedulerInputNameConfiguration
		return ret
	}).(InferenceSchedulerInputNameConfigurationOutput)
}

// Indicates the delimiter character used between items in the data.
func (o InferenceSchedulerInputNameConfigurationPtrOutput) ComponentTimestampDelimiter() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *InferenceSchedulerInputNameConfiguration) *string {
		if v == nil {
			return nil
		}
		return v.ComponentTimestampDelimiter
	}).(pulumi.StringPtrOutput)
}

// The format of the timestamp, whether Epoch time, or standard, with or without hyphens (-).
func (o InferenceSchedulerInputNameConfigurationPtrOutput) TimestampFormat() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *InferenceSchedulerInputNameConfiguration) *string {
		if v == nil {
			return nil
		}
		return v.TimestampFormat
	}).(pulumi.StringPtrOutput)
}

// Specifies configuration information for the input data for the inference, including input data S3 location.
type InferenceSchedulerS3InputConfiguration struct {
	Bucket string  `pulumi:"bucket"`
	Prefix *string `pulumi:"prefix"`
}

// InferenceSchedulerS3InputConfigurationInput is an input type that accepts InferenceSchedulerS3InputConfigurationArgs and InferenceSchedulerS3InputConfigurationOutput values.
// You can construct a concrete instance of `InferenceSchedulerS3InputConfigurationInput` via:
//
//	InferenceSchedulerS3InputConfigurationArgs{...}
type InferenceSchedulerS3InputConfigurationInput interface {
	pulumi.Input

	ToInferenceSchedulerS3InputConfigurationOutput() InferenceSchedulerS3InputConfigurationOutput
	ToInferenceSchedulerS3InputConfigurationOutputWithContext(context.Context) InferenceSchedulerS3InputConfigurationOutput
}

// Specifies configuration information for the input data for the inference, including input data S3 location.
type InferenceSchedulerS3InputConfigurationArgs struct {
	Bucket pulumi.StringInput    `pulumi:"bucket"`
	Prefix pulumi.StringPtrInput `pulumi:"prefix"`
}

func (InferenceSchedulerS3InputConfigurationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*InferenceSchedulerS3InputConfiguration)(nil)).Elem()
}

func (i InferenceSchedulerS3InputConfigurationArgs) ToInferenceSchedulerS3InputConfigurationOutput() InferenceSchedulerS3InputConfigurationOutput {
	return i.ToInferenceSchedulerS3InputConfigurationOutputWithContext(context.Background())
}

func (i InferenceSchedulerS3InputConfigurationArgs) ToInferenceSchedulerS3InputConfigurationOutputWithContext(ctx context.Context) InferenceSchedulerS3InputConfigurationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(InferenceSchedulerS3InputConfigurationOutput)
}

// Specifies configuration information for the input data for the inference, including input data S3 location.
type InferenceSchedulerS3InputConfigurationOutput struct{ *pulumi.OutputState }

func (InferenceSchedulerS3InputConfigurationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*InferenceSchedulerS3InputConfiguration)(nil)).Elem()
}

func (o InferenceSchedulerS3InputConfigurationOutput) ToInferenceSchedulerS3InputConfigurationOutput() InferenceSchedulerS3InputConfigurationOutput {
	return o
}

func (o InferenceSchedulerS3InputConfigurationOutput) ToInferenceSchedulerS3InputConfigurationOutputWithContext(ctx context.Context) InferenceSchedulerS3InputConfigurationOutput {
	return o
}

func (o InferenceSchedulerS3InputConfigurationOutput) Bucket() pulumi.StringOutput {
	return o.ApplyT(func(v InferenceSchedulerS3InputConfiguration) string { return v.Bucket }).(pulumi.StringOutput)
}

func (o InferenceSchedulerS3InputConfigurationOutput) Prefix() pulumi.StringPtrOutput {
	return o.ApplyT(func(v InferenceSchedulerS3InputConfiguration) *string { return v.Prefix }).(pulumi.StringPtrOutput)
}

type InferenceSchedulerS3InputConfigurationPtrOutput struct{ *pulumi.OutputState }

func (InferenceSchedulerS3InputConfigurationPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**InferenceSchedulerS3InputConfiguration)(nil)).Elem()
}

func (o InferenceSchedulerS3InputConfigurationPtrOutput) ToInferenceSchedulerS3InputConfigurationPtrOutput() InferenceSchedulerS3InputConfigurationPtrOutput {
	return o
}

func (o InferenceSchedulerS3InputConfigurationPtrOutput) ToInferenceSchedulerS3InputConfigurationPtrOutputWithContext(ctx context.Context) InferenceSchedulerS3InputConfigurationPtrOutput {
	return o
}

func (o InferenceSchedulerS3InputConfigurationPtrOutput) Elem() InferenceSchedulerS3InputConfigurationOutput {
	return o.ApplyT(func(v *InferenceSchedulerS3InputConfiguration) InferenceSchedulerS3InputConfiguration {
		if v != nil {
			return *v
		}
		var ret InferenceSchedulerS3InputConfiguration
		return ret
	}).(InferenceSchedulerS3InputConfigurationOutput)
}

func (o InferenceSchedulerS3InputConfigurationPtrOutput) Bucket() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *InferenceSchedulerS3InputConfiguration) *string {
		if v == nil {
			return nil
		}
		return &v.Bucket
	}).(pulumi.StringPtrOutput)
}

func (o InferenceSchedulerS3InputConfigurationPtrOutput) Prefix() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *InferenceSchedulerS3InputConfiguration) *string {
		if v == nil {
			return nil
		}
		return v.Prefix
	}).(pulumi.StringPtrOutput)
}

// Specifies configuration information for the output results from the inference, including output S3 location.
type InferenceSchedulerS3OutputConfiguration struct {
	Bucket string  `pulumi:"bucket"`
	Prefix *string `pulumi:"prefix"`
}

// InferenceSchedulerS3OutputConfigurationInput is an input type that accepts InferenceSchedulerS3OutputConfigurationArgs and InferenceSchedulerS3OutputConfigurationOutput values.
// You can construct a concrete instance of `InferenceSchedulerS3OutputConfigurationInput` via:
//
//	InferenceSchedulerS3OutputConfigurationArgs{...}
type InferenceSchedulerS3OutputConfigurationInput interface {
	pulumi.Input

	ToInferenceSchedulerS3OutputConfigurationOutput() InferenceSchedulerS3OutputConfigurationOutput
	ToInferenceSchedulerS3OutputConfigurationOutputWithContext(context.Context) InferenceSchedulerS3OutputConfigurationOutput
}

// Specifies configuration information for the output results from the inference, including output S3 location.
type InferenceSchedulerS3OutputConfigurationArgs struct {
	Bucket pulumi.StringInput    `pulumi:"bucket"`
	Prefix pulumi.StringPtrInput `pulumi:"prefix"`
}

func (InferenceSchedulerS3OutputConfigurationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*InferenceSchedulerS3OutputConfiguration)(nil)).Elem()
}

func (i InferenceSchedulerS3OutputConfigurationArgs) ToInferenceSchedulerS3OutputConfigurationOutput() InferenceSchedulerS3OutputConfigurationOutput {
	return i.ToInferenceSchedulerS3OutputConfigurationOutputWithContext(context.Background())
}

func (i InferenceSchedulerS3OutputConfigurationArgs) ToInferenceSchedulerS3OutputConfigurationOutputWithContext(ctx context.Context) InferenceSchedulerS3OutputConfigurationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(InferenceSchedulerS3OutputConfigurationOutput)
}

// Specifies configuration information for the output results from the inference, including output S3 location.
type InferenceSchedulerS3OutputConfigurationOutput struct{ *pulumi.OutputState }

func (InferenceSchedulerS3OutputConfigurationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*InferenceSchedulerS3OutputConfiguration)(nil)).Elem()
}

func (o InferenceSchedulerS3OutputConfigurationOutput) ToInferenceSchedulerS3OutputConfigurationOutput() InferenceSchedulerS3OutputConfigurationOutput {
	return o
}

func (o InferenceSchedulerS3OutputConfigurationOutput) ToInferenceSchedulerS3OutputConfigurationOutputWithContext(ctx context.Context) InferenceSchedulerS3OutputConfigurationOutput {
	return o
}

func (o InferenceSchedulerS3OutputConfigurationOutput) Bucket() pulumi.StringOutput {
	return o.ApplyT(func(v InferenceSchedulerS3OutputConfiguration) string { return v.Bucket }).(pulumi.StringOutput)
}

func (o InferenceSchedulerS3OutputConfigurationOutput) Prefix() pulumi.StringPtrOutput {
	return o.ApplyT(func(v InferenceSchedulerS3OutputConfiguration) *string { return v.Prefix }).(pulumi.StringPtrOutput)
}

type InferenceSchedulerS3OutputConfigurationPtrOutput struct{ *pulumi.OutputState }

func (InferenceSchedulerS3OutputConfigurationPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**InferenceSchedulerS3OutputConfiguration)(nil)).Elem()
}

func (o InferenceSchedulerS3OutputConfigurationPtrOutput) ToInferenceSchedulerS3OutputConfigurationPtrOutput() InferenceSchedulerS3OutputConfigurationPtrOutput {
	return o
}

func (o InferenceSchedulerS3OutputConfigurationPtrOutput) ToInferenceSchedulerS3OutputConfigurationPtrOutputWithContext(ctx context.Context) InferenceSchedulerS3OutputConfigurationPtrOutput {
	return o
}

func (o InferenceSchedulerS3OutputConfigurationPtrOutput) Elem() InferenceSchedulerS3OutputConfigurationOutput {
	return o.ApplyT(func(v *InferenceSchedulerS3OutputConfiguration) InferenceSchedulerS3OutputConfiguration {
		if v != nil {
			return *v
		}
		var ret InferenceSchedulerS3OutputConfiguration
		return ret
	}).(InferenceSchedulerS3OutputConfigurationOutput)
}

func (o InferenceSchedulerS3OutputConfigurationPtrOutput) Bucket() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *InferenceSchedulerS3OutputConfiguration) *string {
		if v == nil {
			return nil
		}
		return &v.Bucket
	}).(pulumi.StringPtrOutput)
}

func (o InferenceSchedulerS3OutputConfigurationPtrOutput) Prefix() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *InferenceSchedulerS3OutputConfiguration) *string {
		if v == nil {
			return nil
		}
		return v.Prefix
	}).(pulumi.StringPtrOutput)
}

// A tag is a key-value pair that can be added to a resource as metadata.
type InferenceSchedulerTag struct {
	// The key for the specified tag.
	Key string `pulumi:"key"`
	// The value for the specified tag.
	Value string `pulumi:"value"`
}

// InferenceSchedulerTagInput is an input type that accepts InferenceSchedulerTagArgs and InferenceSchedulerTagOutput values.
// You can construct a concrete instance of `InferenceSchedulerTagInput` via:
//
//	InferenceSchedulerTagArgs{...}
type InferenceSchedulerTagInput interface {
	pulumi.Input

	ToInferenceSchedulerTagOutput() InferenceSchedulerTagOutput
	ToInferenceSchedulerTagOutputWithContext(context.Context) InferenceSchedulerTagOutput
}

// A tag is a key-value pair that can be added to a resource as metadata.
type InferenceSchedulerTagArgs struct {
	// The key for the specified tag.
	Key pulumi.StringInput `pulumi:"key"`
	// The value for the specified tag.
	Value pulumi.StringInput `pulumi:"value"`
}

func (InferenceSchedulerTagArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*InferenceSchedulerTag)(nil)).Elem()
}

func (i InferenceSchedulerTagArgs) ToInferenceSchedulerTagOutput() InferenceSchedulerTagOutput {
	return i.ToInferenceSchedulerTagOutputWithContext(context.Background())
}

func (i InferenceSchedulerTagArgs) ToInferenceSchedulerTagOutputWithContext(ctx context.Context) InferenceSchedulerTagOutput {
	return pulumi.ToOutputWithContext(ctx, i).(InferenceSchedulerTagOutput)
}

// InferenceSchedulerTagArrayInput is an input type that accepts InferenceSchedulerTagArray and InferenceSchedulerTagArrayOutput values.
// You can construct a concrete instance of `InferenceSchedulerTagArrayInput` via:
//
//	InferenceSchedulerTagArray{ InferenceSchedulerTagArgs{...} }
type InferenceSchedulerTagArrayInput interface {
	pulumi.Input

	ToInferenceSchedulerTagArrayOutput() InferenceSchedulerTagArrayOutput
	ToInferenceSchedulerTagArrayOutputWithContext(context.Context) InferenceSchedulerTagArrayOutput
}

type InferenceSchedulerTagArray []InferenceSchedulerTagInput

func (InferenceSchedulerTagArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]InferenceSchedulerTag)(nil)).Elem()
}

func (i InferenceSchedulerTagArray) ToInferenceSchedulerTagArrayOutput() InferenceSchedulerTagArrayOutput {
	return i.ToInferenceSchedulerTagArrayOutputWithContext(context.Background())
}

func (i InferenceSchedulerTagArray) ToInferenceSchedulerTagArrayOutputWithContext(ctx context.Context) InferenceSchedulerTagArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(InferenceSchedulerTagArrayOutput)
}

// A tag is a key-value pair that can be added to a resource as metadata.
type InferenceSchedulerTagOutput struct{ *pulumi.OutputState }

func (InferenceSchedulerTagOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*InferenceSchedulerTag)(nil)).Elem()
}

func (o InferenceSchedulerTagOutput) ToInferenceSchedulerTagOutput() InferenceSchedulerTagOutput {
	return o
}

func (o InferenceSchedulerTagOutput) ToInferenceSchedulerTagOutputWithContext(ctx context.Context) InferenceSchedulerTagOutput {
	return o
}

// The key for the specified tag.
func (o InferenceSchedulerTagOutput) Key() pulumi.StringOutput {
	return o.ApplyT(func(v InferenceSchedulerTag) string { return v.Key }).(pulumi.StringOutput)
}

// The value for the specified tag.
func (o InferenceSchedulerTagOutput) Value() pulumi.StringOutput {
	return o.ApplyT(func(v InferenceSchedulerTag) string { return v.Value }).(pulumi.StringOutput)
}

type InferenceSchedulerTagArrayOutput struct{ *pulumi.OutputState }

func (InferenceSchedulerTagArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]InferenceSchedulerTag)(nil)).Elem()
}

func (o InferenceSchedulerTagArrayOutput) ToInferenceSchedulerTagArrayOutput() InferenceSchedulerTagArrayOutput {
	return o
}

func (o InferenceSchedulerTagArrayOutput) ToInferenceSchedulerTagArrayOutputWithContext(ctx context.Context) InferenceSchedulerTagArrayOutput {
	return o
}

func (o InferenceSchedulerTagArrayOutput) Index(i pulumi.IntInput) InferenceSchedulerTagOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) InferenceSchedulerTag {
		return vs[0].([]InferenceSchedulerTag)[vs[1].(int)]
	}).(InferenceSchedulerTagOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*DataInputConfigurationPropertiesInput)(nil)).Elem(), DataInputConfigurationPropertiesArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*DataOutputConfigurationPropertiesInput)(nil)).Elem(), DataOutputConfigurationPropertiesArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*InferenceSchedulerInputNameConfigurationInput)(nil)).Elem(), InferenceSchedulerInputNameConfigurationArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*InferenceSchedulerInputNameConfigurationPtrInput)(nil)).Elem(), InferenceSchedulerInputNameConfigurationArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*InferenceSchedulerS3InputConfigurationInput)(nil)).Elem(), InferenceSchedulerS3InputConfigurationArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*InferenceSchedulerS3OutputConfigurationInput)(nil)).Elem(), InferenceSchedulerS3OutputConfigurationArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*InferenceSchedulerTagInput)(nil)).Elem(), InferenceSchedulerTagArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*InferenceSchedulerTagArrayInput)(nil)).Elem(), InferenceSchedulerTagArray{})
	pulumi.RegisterOutputType(DataInputConfigurationPropertiesOutput{})
	pulumi.RegisterOutputType(DataInputConfigurationPropertiesPtrOutput{})
	pulumi.RegisterOutputType(DataOutputConfigurationPropertiesOutput{})
	pulumi.RegisterOutputType(DataOutputConfigurationPropertiesPtrOutput{})
	pulumi.RegisterOutputType(InferenceSchedulerInputNameConfigurationOutput{})
	pulumi.RegisterOutputType(InferenceSchedulerInputNameConfigurationPtrOutput{})
	pulumi.RegisterOutputType(InferenceSchedulerS3InputConfigurationOutput{})
	pulumi.RegisterOutputType(InferenceSchedulerS3InputConfigurationPtrOutput{})
	pulumi.RegisterOutputType(InferenceSchedulerS3OutputConfigurationOutput{})
	pulumi.RegisterOutputType(InferenceSchedulerS3OutputConfigurationPtrOutput{})
	pulumi.RegisterOutputType(InferenceSchedulerTagOutput{})
	pulumi.RegisterOutputType(InferenceSchedulerTagArrayOutput{})
}
