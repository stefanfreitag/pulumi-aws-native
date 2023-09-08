// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package secretsmanager

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::SecretsManager::RotationSchedule
//
// Deprecated: RotationSchedule is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type RotationSchedule struct {
	pulumi.CustomResourceState

	HostedRotationLambda      RotationScheduleHostedRotationLambdaPtrOutput `pulumi:"hostedRotationLambda"`
	RotateImmediatelyOnUpdate pulumi.BoolPtrOutput                          `pulumi:"rotateImmediatelyOnUpdate"`
	RotationLambdaArn         pulumi.StringPtrOutput                        `pulumi:"rotationLambdaArn"`
	RotationRules             RotationScheduleRotationRulesPtrOutput        `pulumi:"rotationRules"`
	SecretId                  pulumi.StringOutput                           `pulumi:"secretId"`
}

// NewRotationSchedule registers a new resource with the given unique name, arguments, and options.
func NewRotationSchedule(ctx *pulumi.Context,
	name string, args *RotationScheduleArgs, opts ...pulumi.ResourceOption) (*RotationSchedule, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.SecretId == nil {
		return nil, errors.New("invalid value for required argument 'SecretId'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"secretId",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource RotationSchedule
	err := ctx.RegisterResource("aws-native:secretsmanager:RotationSchedule", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetRotationSchedule gets an existing RotationSchedule resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetRotationSchedule(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *RotationScheduleState, opts ...pulumi.ResourceOption) (*RotationSchedule, error) {
	var resource RotationSchedule
	err := ctx.ReadResource("aws-native:secretsmanager:RotationSchedule", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering RotationSchedule resources.
type rotationScheduleState struct {
}

type RotationScheduleState struct {
}

func (RotationScheduleState) ElementType() reflect.Type {
	return reflect.TypeOf((*rotationScheduleState)(nil)).Elem()
}

type rotationScheduleArgs struct {
	HostedRotationLambda      *RotationScheduleHostedRotationLambda `pulumi:"hostedRotationLambda"`
	RotateImmediatelyOnUpdate *bool                                 `pulumi:"rotateImmediatelyOnUpdate"`
	RotationLambdaArn         *string                               `pulumi:"rotationLambdaArn"`
	RotationRules             *RotationScheduleRotationRules        `pulumi:"rotationRules"`
	SecretId                  string                                `pulumi:"secretId"`
}

// The set of arguments for constructing a RotationSchedule resource.
type RotationScheduleArgs struct {
	HostedRotationLambda      RotationScheduleHostedRotationLambdaPtrInput
	RotateImmediatelyOnUpdate pulumi.BoolPtrInput
	RotationLambdaArn         pulumi.StringPtrInput
	RotationRules             RotationScheduleRotationRulesPtrInput
	SecretId                  pulumi.StringInput
}

func (RotationScheduleArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*rotationScheduleArgs)(nil)).Elem()
}

type RotationScheduleInput interface {
	pulumi.Input

	ToRotationScheduleOutput() RotationScheduleOutput
	ToRotationScheduleOutputWithContext(ctx context.Context) RotationScheduleOutput
}

func (*RotationSchedule) ElementType() reflect.Type {
	return reflect.TypeOf((**RotationSchedule)(nil)).Elem()
}

func (i *RotationSchedule) ToRotationScheduleOutput() RotationScheduleOutput {
	return i.ToRotationScheduleOutputWithContext(context.Background())
}

func (i *RotationSchedule) ToRotationScheduleOutputWithContext(ctx context.Context) RotationScheduleOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RotationScheduleOutput)
}

func (i *RotationSchedule) ToOutput(ctx context.Context) pulumix.Output[*RotationSchedule] {
	return pulumix.Output[*RotationSchedule]{
		OutputState: i.ToRotationScheduleOutputWithContext(ctx).OutputState,
	}
}

type RotationScheduleOutput struct{ *pulumi.OutputState }

func (RotationScheduleOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**RotationSchedule)(nil)).Elem()
}

func (o RotationScheduleOutput) ToRotationScheduleOutput() RotationScheduleOutput {
	return o
}

func (o RotationScheduleOutput) ToRotationScheduleOutputWithContext(ctx context.Context) RotationScheduleOutput {
	return o
}

func (o RotationScheduleOutput) ToOutput(ctx context.Context) pulumix.Output[*RotationSchedule] {
	return pulumix.Output[*RotationSchedule]{
		OutputState: o.OutputState,
	}
}

func (o RotationScheduleOutput) HostedRotationLambda() RotationScheduleHostedRotationLambdaPtrOutput {
	return o.ApplyT(func(v *RotationSchedule) RotationScheduleHostedRotationLambdaPtrOutput { return v.HostedRotationLambda }).(RotationScheduleHostedRotationLambdaPtrOutput)
}

func (o RotationScheduleOutput) RotateImmediatelyOnUpdate() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *RotationSchedule) pulumi.BoolPtrOutput { return v.RotateImmediatelyOnUpdate }).(pulumi.BoolPtrOutput)
}

func (o RotationScheduleOutput) RotationLambdaArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *RotationSchedule) pulumi.StringPtrOutput { return v.RotationLambdaArn }).(pulumi.StringPtrOutput)
}

func (o RotationScheduleOutput) RotationRules() RotationScheduleRotationRulesPtrOutput {
	return o.ApplyT(func(v *RotationSchedule) RotationScheduleRotationRulesPtrOutput { return v.RotationRules }).(RotationScheduleRotationRulesPtrOutput)
}

func (o RotationScheduleOutput) SecretId() pulumi.StringOutput {
	return o.ApplyT(func(v *RotationSchedule) pulumi.StringOutput { return v.SecretId }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*RotationScheduleInput)(nil)).Elem(), &RotationSchedule{})
	pulumi.RegisterOutputType(RotationScheduleOutput{})
}
