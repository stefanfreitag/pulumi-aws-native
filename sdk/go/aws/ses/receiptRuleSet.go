// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ses

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::SES::ReceiptRuleSet
//
// Deprecated: ReceiptRuleSet is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type ReceiptRuleSet struct {
	pulumi.CustomResourceState

	RuleSetName pulumi.StringPtrOutput `pulumi:"ruleSetName"`
}

// NewReceiptRuleSet registers a new resource with the given unique name, arguments, and options.
func NewReceiptRuleSet(ctx *pulumi.Context,
	name string, args *ReceiptRuleSetArgs, opts ...pulumi.ResourceOption) (*ReceiptRuleSet, error) {
	if args == nil {
		args = &ReceiptRuleSetArgs{}
	}

	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"ruleSetName",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource ReceiptRuleSet
	err := ctx.RegisterResource("aws-native:ses:ReceiptRuleSet", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetReceiptRuleSet gets an existing ReceiptRuleSet resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetReceiptRuleSet(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ReceiptRuleSetState, opts ...pulumi.ResourceOption) (*ReceiptRuleSet, error) {
	var resource ReceiptRuleSet
	err := ctx.ReadResource("aws-native:ses:ReceiptRuleSet", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ReceiptRuleSet resources.
type receiptRuleSetState struct {
}

type ReceiptRuleSetState struct {
}

func (ReceiptRuleSetState) ElementType() reflect.Type {
	return reflect.TypeOf((*receiptRuleSetState)(nil)).Elem()
}

type receiptRuleSetArgs struct {
	RuleSetName *string `pulumi:"ruleSetName"`
}

// The set of arguments for constructing a ReceiptRuleSet resource.
type ReceiptRuleSetArgs struct {
	RuleSetName pulumi.StringPtrInput
}

func (ReceiptRuleSetArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*receiptRuleSetArgs)(nil)).Elem()
}

type ReceiptRuleSetInput interface {
	pulumi.Input

	ToReceiptRuleSetOutput() ReceiptRuleSetOutput
	ToReceiptRuleSetOutputWithContext(ctx context.Context) ReceiptRuleSetOutput
}

func (*ReceiptRuleSet) ElementType() reflect.Type {
	return reflect.TypeOf((**ReceiptRuleSet)(nil)).Elem()
}

func (i *ReceiptRuleSet) ToReceiptRuleSetOutput() ReceiptRuleSetOutput {
	return i.ToReceiptRuleSetOutputWithContext(context.Background())
}

func (i *ReceiptRuleSet) ToReceiptRuleSetOutputWithContext(ctx context.Context) ReceiptRuleSetOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ReceiptRuleSetOutput)
}

func (i *ReceiptRuleSet) ToOutput(ctx context.Context) pulumix.Output[*ReceiptRuleSet] {
	return pulumix.Output[*ReceiptRuleSet]{
		OutputState: i.ToReceiptRuleSetOutputWithContext(ctx).OutputState,
	}
}

type ReceiptRuleSetOutput struct{ *pulumi.OutputState }

func (ReceiptRuleSetOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ReceiptRuleSet)(nil)).Elem()
}

func (o ReceiptRuleSetOutput) ToReceiptRuleSetOutput() ReceiptRuleSetOutput {
	return o
}

func (o ReceiptRuleSetOutput) ToReceiptRuleSetOutputWithContext(ctx context.Context) ReceiptRuleSetOutput {
	return o
}

func (o ReceiptRuleSetOutput) ToOutput(ctx context.Context) pulumix.Output[*ReceiptRuleSet] {
	return pulumix.Output[*ReceiptRuleSet]{
		OutputState: o.OutputState,
	}
}

func (o ReceiptRuleSetOutput) RuleSetName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ReceiptRuleSet) pulumi.StringPtrOutput { return v.RuleSetName }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ReceiptRuleSetInput)(nil)).Elem(), &ReceiptRuleSet{})
	pulumi.RegisterOutputType(ReceiptRuleSetOutput{})
}
