// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package kendra

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// A Kendra FAQ resource
type Faq struct {
	pulumi.CustomResourceState

	Arn pulumi.StringOutput `pulumi:"arn"`
	// FAQ description
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// FAQ file format
	FileFormat FaqFileFormatPtrOutput `pulumi:"fileFormat"`
	// Index ID
	IndexId pulumi.StringOutput `pulumi:"indexId"`
	// FAQ name
	Name pulumi.StringOutput `pulumi:"name"`
	// FAQ role ARN
	RoleArn pulumi.StringOutput `pulumi:"roleArn"`
	// FAQ S3 path
	S3Path FaqS3PathOutput `pulumi:"s3Path"`
	// Tags for labeling the FAQ
	Tags FaqTagArrayOutput `pulumi:"tags"`
}

// NewFaq registers a new resource with the given unique name, arguments, and options.
func NewFaq(ctx *pulumi.Context,
	name string, args *FaqArgs, opts ...pulumi.ResourceOption) (*Faq, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.IndexId == nil {
		return nil, errors.New("invalid value for required argument 'IndexId'")
	}
	if args.RoleArn == nil {
		return nil, errors.New("invalid value for required argument 'RoleArn'")
	}
	if args.S3Path == nil {
		return nil, errors.New("invalid value for required argument 'S3Path'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"description",
		"fileFormat",
		"indexId",
		"name",
		"roleArn",
		"s3Path",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Faq
	err := ctx.RegisterResource("aws-native:kendra:Faq", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetFaq gets an existing Faq resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetFaq(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *FaqState, opts ...pulumi.ResourceOption) (*Faq, error) {
	var resource Faq
	err := ctx.ReadResource("aws-native:kendra:Faq", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Faq resources.
type faqState struct {
}

type FaqState struct {
}

func (FaqState) ElementType() reflect.Type {
	return reflect.TypeOf((*faqState)(nil)).Elem()
}

type faqArgs struct {
	// FAQ description
	Description *string `pulumi:"description"`
	// FAQ file format
	FileFormat *FaqFileFormat `pulumi:"fileFormat"`
	// Index ID
	IndexId string `pulumi:"indexId"`
	// FAQ name
	Name *string `pulumi:"name"`
	// FAQ role ARN
	RoleArn string `pulumi:"roleArn"`
	// FAQ S3 path
	S3Path FaqS3Path `pulumi:"s3Path"`
	// Tags for labeling the FAQ
	Tags []FaqTag `pulumi:"tags"`
}

// The set of arguments for constructing a Faq resource.
type FaqArgs struct {
	// FAQ description
	Description pulumi.StringPtrInput
	// FAQ file format
	FileFormat FaqFileFormatPtrInput
	// Index ID
	IndexId pulumi.StringInput
	// FAQ name
	Name pulumi.StringPtrInput
	// FAQ role ARN
	RoleArn pulumi.StringInput
	// FAQ S3 path
	S3Path FaqS3PathInput
	// Tags for labeling the FAQ
	Tags FaqTagArrayInput
}

func (FaqArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*faqArgs)(nil)).Elem()
}

type FaqInput interface {
	pulumi.Input

	ToFaqOutput() FaqOutput
	ToFaqOutputWithContext(ctx context.Context) FaqOutput
}

func (*Faq) ElementType() reflect.Type {
	return reflect.TypeOf((**Faq)(nil)).Elem()
}

func (i *Faq) ToFaqOutput() FaqOutput {
	return i.ToFaqOutputWithContext(context.Background())
}

func (i *Faq) ToFaqOutputWithContext(ctx context.Context) FaqOutput {
	return pulumi.ToOutputWithContext(ctx, i).(FaqOutput)
}

func (i *Faq) ToOutput(ctx context.Context) pulumix.Output[*Faq] {
	return pulumix.Output[*Faq]{
		OutputState: i.ToFaqOutputWithContext(ctx).OutputState,
	}
}

type FaqOutput struct{ *pulumi.OutputState }

func (FaqOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Faq)(nil)).Elem()
}

func (o FaqOutput) ToFaqOutput() FaqOutput {
	return o
}

func (o FaqOutput) ToFaqOutputWithContext(ctx context.Context) FaqOutput {
	return o
}

func (o FaqOutput) ToOutput(ctx context.Context) pulumix.Output[*Faq] {
	return pulumix.Output[*Faq]{
		OutputState: o.OutputState,
	}
}

func (o FaqOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *Faq) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

// FAQ description
func (o FaqOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Faq) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// FAQ file format
func (o FaqOutput) FileFormat() FaqFileFormatPtrOutput {
	return o.ApplyT(func(v *Faq) FaqFileFormatPtrOutput { return v.FileFormat }).(FaqFileFormatPtrOutput)
}

// Index ID
func (o FaqOutput) IndexId() pulumi.StringOutput {
	return o.ApplyT(func(v *Faq) pulumi.StringOutput { return v.IndexId }).(pulumi.StringOutput)
}

// FAQ name
func (o FaqOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Faq) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// FAQ role ARN
func (o FaqOutput) RoleArn() pulumi.StringOutput {
	return o.ApplyT(func(v *Faq) pulumi.StringOutput { return v.RoleArn }).(pulumi.StringOutput)
}

// FAQ S3 path
func (o FaqOutput) S3Path() FaqS3PathOutput {
	return o.ApplyT(func(v *Faq) FaqS3PathOutput { return v.S3Path }).(FaqS3PathOutput)
}

// Tags for labeling the FAQ
func (o FaqOutput) Tags() FaqTagArrayOutput {
	return o.ApplyT(func(v *Faq) FaqTagArrayOutput { return v.Tags }).(FaqTagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*FaqInput)(nil)).Elem(), &Faq{})
	pulumi.RegisterOutputType(FaqOutput{})
}
