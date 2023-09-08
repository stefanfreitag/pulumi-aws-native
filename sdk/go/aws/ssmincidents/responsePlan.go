// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ssmincidents

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource type definition for AWS::SSMIncidents::ResponsePlan
type ResponsePlan struct {
	pulumi.CustomResourceState

	// The list of actions.
	Actions ResponsePlanActionArrayOutput `pulumi:"actions"`
	// The ARN of the response plan.
	Arn         pulumi.StringOutput              `pulumi:"arn"`
	ChatChannel ResponsePlanChatChannelPtrOutput `pulumi:"chatChannel"`
	// The display name of the response plan.
	DisplayName pulumi.StringPtrOutput `pulumi:"displayName"`
	// The list of engagements to use.
	Engagements      pulumi.StringArrayOutput           `pulumi:"engagements"`
	IncidentTemplate ResponsePlanIncidentTemplateOutput `pulumi:"incidentTemplate"`
	// The list of integrations.
	Integrations ResponsePlanIntegrationArrayOutput `pulumi:"integrations"`
	// The name of the response plan.
	Name pulumi.StringOutput `pulumi:"name"`
	// The tags to apply to the response plan.
	Tags ResponsePlanTagArrayOutput `pulumi:"tags"`
}

// NewResponsePlan registers a new resource with the given unique name, arguments, and options.
func NewResponsePlan(ctx *pulumi.Context,
	name string, args *ResponsePlanArgs, opts ...pulumi.ResourceOption) (*ResponsePlan, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.IncidentTemplate == nil {
		return nil, errors.New("invalid value for required argument 'IncidentTemplate'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"name",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource ResponsePlan
	err := ctx.RegisterResource("aws-native:ssmincidents:ResponsePlan", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetResponsePlan gets an existing ResponsePlan resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetResponsePlan(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ResponsePlanState, opts ...pulumi.ResourceOption) (*ResponsePlan, error) {
	var resource ResponsePlan
	err := ctx.ReadResource("aws-native:ssmincidents:ResponsePlan", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ResponsePlan resources.
type responsePlanState struct {
}

type ResponsePlanState struct {
}

func (ResponsePlanState) ElementType() reflect.Type {
	return reflect.TypeOf((*responsePlanState)(nil)).Elem()
}

type responsePlanArgs struct {
	// The list of actions.
	Actions     []ResponsePlanAction     `pulumi:"actions"`
	ChatChannel *ResponsePlanChatChannel `pulumi:"chatChannel"`
	// The display name of the response plan.
	DisplayName *string `pulumi:"displayName"`
	// The list of engagements to use.
	Engagements      []string                     `pulumi:"engagements"`
	IncidentTemplate ResponsePlanIncidentTemplate `pulumi:"incidentTemplate"`
	// The list of integrations.
	Integrations []ResponsePlanIntegration `pulumi:"integrations"`
	// The name of the response plan.
	Name *string `pulumi:"name"`
	// The tags to apply to the response plan.
	Tags []ResponsePlanTag `pulumi:"tags"`
}

// The set of arguments for constructing a ResponsePlan resource.
type ResponsePlanArgs struct {
	// The list of actions.
	Actions     ResponsePlanActionArrayInput
	ChatChannel ResponsePlanChatChannelPtrInput
	// The display name of the response plan.
	DisplayName pulumi.StringPtrInput
	// The list of engagements to use.
	Engagements      pulumi.StringArrayInput
	IncidentTemplate ResponsePlanIncidentTemplateInput
	// The list of integrations.
	Integrations ResponsePlanIntegrationArrayInput
	// The name of the response plan.
	Name pulumi.StringPtrInput
	// The tags to apply to the response plan.
	Tags ResponsePlanTagArrayInput
}

func (ResponsePlanArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*responsePlanArgs)(nil)).Elem()
}

type ResponsePlanInput interface {
	pulumi.Input

	ToResponsePlanOutput() ResponsePlanOutput
	ToResponsePlanOutputWithContext(ctx context.Context) ResponsePlanOutput
}

func (*ResponsePlan) ElementType() reflect.Type {
	return reflect.TypeOf((**ResponsePlan)(nil)).Elem()
}

func (i *ResponsePlan) ToResponsePlanOutput() ResponsePlanOutput {
	return i.ToResponsePlanOutputWithContext(context.Background())
}

func (i *ResponsePlan) ToResponsePlanOutputWithContext(ctx context.Context) ResponsePlanOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ResponsePlanOutput)
}

func (i *ResponsePlan) ToOutput(ctx context.Context) pulumix.Output[*ResponsePlan] {
	return pulumix.Output[*ResponsePlan]{
		OutputState: i.ToResponsePlanOutputWithContext(ctx).OutputState,
	}
}

type ResponsePlanOutput struct{ *pulumi.OutputState }

func (ResponsePlanOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ResponsePlan)(nil)).Elem()
}

func (o ResponsePlanOutput) ToResponsePlanOutput() ResponsePlanOutput {
	return o
}

func (o ResponsePlanOutput) ToResponsePlanOutputWithContext(ctx context.Context) ResponsePlanOutput {
	return o
}

func (o ResponsePlanOutput) ToOutput(ctx context.Context) pulumix.Output[*ResponsePlan] {
	return pulumix.Output[*ResponsePlan]{
		OutputState: o.OutputState,
	}
}

// The list of actions.
func (o ResponsePlanOutput) Actions() ResponsePlanActionArrayOutput {
	return o.ApplyT(func(v *ResponsePlan) ResponsePlanActionArrayOutput { return v.Actions }).(ResponsePlanActionArrayOutput)
}

// The ARN of the response plan.
func (o ResponsePlanOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *ResponsePlan) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

func (o ResponsePlanOutput) ChatChannel() ResponsePlanChatChannelPtrOutput {
	return o.ApplyT(func(v *ResponsePlan) ResponsePlanChatChannelPtrOutput { return v.ChatChannel }).(ResponsePlanChatChannelPtrOutput)
}

// The display name of the response plan.
func (o ResponsePlanOutput) DisplayName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ResponsePlan) pulumi.StringPtrOutput { return v.DisplayName }).(pulumi.StringPtrOutput)
}

// The list of engagements to use.
func (o ResponsePlanOutput) Engagements() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *ResponsePlan) pulumi.StringArrayOutput { return v.Engagements }).(pulumi.StringArrayOutput)
}

func (o ResponsePlanOutput) IncidentTemplate() ResponsePlanIncidentTemplateOutput {
	return o.ApplyT(func(v *ResponsePlan) ResponsePlanIncidentTemplateOutput { return v.IncidentTemplate }).(ResponsePlanIncidentTemplateOutput)
}

// The list of integrations.
func (o ResponsePlanOutput) Integrations() ResponsePlanIntegrationArrayOutput {
	return o.ApplyT(func(v *ResponsePlan) ResponsePlanIntegrationArrayOutput { return v.Integrations }).(ResponsePlanIntegrationArrayOutput)
}

// The name of the response plan.
func (o ResponsePlanOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *ResponsePlan) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The tags to apply to the response plan.
func (o ResponsePlanOutput) Tags() ResponsePlanTagArrayOutput {
	return o.ApplyT(func(v *ResponsePlan) ResponsePlanTagArrayOutput { return v.Tags }).(ResponsePlanTagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ResponsePlanInput)(nil)).Elem(), &ResponsePlan{})
	pulumi.RegisterOutputType(ResponsePlanOutput{})
}
