// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package pinpoint

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::Pinpoint::SmsTemplate
//
// Deprecated: SmsTemplate is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type SmsTemplate struct {
	pulumi.CustomResourceState

	Arn                  pulumi.StringOutput    `pulumi:"arn"`
	Body                 pulumi.StringOutput    `pulumi:"body"`
	DefaultSubstitutions pulumi.StringPtrOutput `pulumi:"defaultSubstitutions"`
	// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Pinpoint::SmsTemplate` for more information about the expected schema for this property.
	Tags                pulumi.AnyOutput       `pulumi:"tags"`
	TemplateDescription pulumi.StringPtrOutput `pulumi:"templateDescription"`
	TemplateName        pulumi.StringOutput    `pulumi:"templateName"`
}

// NewSmsTemplate registers a new resource with the given unique name, arguments, and options.
func NewSmsTemplate(ctx *pulumi.Context,
	name string, args *SmsTemplateArgs, opts ...pulumi.ResourceOption) (*SmsTemplate, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Body == nil {
		return nil, errors.New("invalid value for required argument 'Body'")
	}
	if args.TemplateName == nil {
		return nil, errors.New("invalid value for required argument 'TemplateName'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"templateName",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource SmsTemplate
	err := ctx.RegisterResource("aws-native:pinpoint:SmsTemplate", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSmsTemplate gets an existing SmsTemplate resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSmsTemplate(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SmsTemplateState, opts ...pulumi.ResourceOption) (*SmsTemplate, error) {
	var resource SmsTemplate
	err := ctx.ReadResource("aws-native:pinpoint:SmsTemplate", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering SmsTemplate resources.
type smsTemplateState struct {
}

type SmsTemplateState struct {
}

func (SmsTemplateState) ElementType() reflect.Type {
	return reflect.TypeOf((*smsTemplateState)(nil)).Elem()
}

type smsTemplateArgs struct {
	Body                 string  `pulumi:"body"`
	DefaultSubstitutions *string `pulumi:"defaultSubstitutions"`
	// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Pinpoint::SmsTemplate` for more information about the expected schema for this property.
	Tags                interface{} `pulumi:"tags"`
	TemplateDescription *string     `pulumi:"templateDescription"`
	TemplateName        string      `pulumi:"templateName"`
}

// The set of arguments for constructing a SmsTemplate resource.
type SmsTemplateArgs struct {
	Body                 pulumi.StringInput
	DefaultSubstitutions pulumi.StringPtrInput
	// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Pinpoint::SmsTemplate` for more information about the expected schema for this property.
	Tags                pulumi.Input
	TemplateDescription pulumi.StringPtrInput
	TemplateName        pulumi.StringInput
}

func (SmsTemplateArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*smsTemplateArgs)(nil)).Elem()
}

type SmsTemplateInput interface {
	pulumi.Input

	ToSmsTemplateOutput() SmsTemplateOutput
	ToSmsTemplateOutputWithContext(ctx context.Context) SmsTemplateOutput
}

func (*SmsTemplate) ElementType() reflect.Type {
	return reflect.TypeOf((**SmsTemplate)(nil)).Elem()
}

func (i *SmsTemplate) ToSmsTemplateOutput() SmsTemplateOutput {
	return i.ToSmsTemplateOutputWithContext(context.Background())
}

func (i *SmsTemplate) ToSmsTemplateOutputWithContext(ctx context.Context) SmsTemplateOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SmsTemplateOutput)
}

type SmsTemplateOutput struct{ *pulumi.OutputState }

func (SmsTemplateOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**SmsTemplate)(nil)).Elem()
}

func (o SmsTemplateOutput) ToSmsTemplateOutput() SmsTemplateOutput {
	return o
}

func (o SmsTemplateOutput) ToSmsTemplateOutputWithContext(ctx context.Context) SmsTemplateOutput {
	return o
}

func (o SmsTemplateOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *SmsTemplate) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

func (o SmsTemplateOutput) Body() pulumi.StringOutput {
	return o.ApplyT(func(v *SmsTemplate) pulumi.StringOutput { return v.Body }).(pulumi.StringOutput)
}

func (o SmsTemplateOutput) DefaultSubstitutions() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *SmsTemplate) pulumi.StringPtrOutput { return v.DefaultSubstitutions }).(pulumi.StringPtrOutput)
}

// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Pinpoint::SmsTemplate` for more information about the expected schema for this property.
func (o SmsTemplateOutput) Tags() pulumi.AnyOutput {
	return o.ApplyT(func(v *SmsTemplate) pulumi.AnyOutput { return v.Tags }).(pulumi.AnyOutput)
}

func (o SmsTemplateOutput) TemplateDescription() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *SmsTemplate) pulumi.StringPtrOutput { return v.TemplateDescription }).(pulumi.StringPtrOutput)
}

func (o SmsTemplateOutput) TemplateName() pulumi.StringOutput {
	return o.ApplyT(func(v *SmsTemplate) pulumi.StringOutput { return v.TemplateName }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*SmsTemplateInput)(nil)).Elem(), &SmsTemplate{})
	pulumi.RegisterOutputType(SmsTemplateOutput{})
}
