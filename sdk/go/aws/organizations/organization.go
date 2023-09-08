// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package organizations

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource schema for AWS::Organizations::Organization
type Organization struct {
	pulumi.CustomResourceState

	// The Amazon Resource Name (ARN) of an organization.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// Specifies the feature set supported by the new organization. Each feature set supports different levels of functionality.
	FeatureSet OrganizationFeatureSetPtrOutput `pulumi:"featureSet"`
	// The Amazon Resource Name (ARN) of the account that is designated as the management account for the organization.
	ManagementAccountArn pulumi.StringOutput `pulumi:"managementAccountArn"`
	// The email address that is associated with the AWS account that is designated as the management account for the organization.
	ManagementAccountEmail pulumi.StringOutput `pulumi:"managementAccountEmail"`
	// The unique identifier (ID) of the management account of an organization.
	ManagementAccountId pulumi.StringOutput `pulumi:"managementAccountId"`
	// The unique identifier (ID) for the root.
	RootId pulumi.StringOutput `pulumi:"rootId"`
}

// NewOrganization registers a new resource with the given unique name, arguments, and options.
func NewOrganization(ctx *pulumi.Context,
	name string, args *OrganizationArgs, opts ...pulumi.ResourceOption) (*Organization, error) {
	if args == nil {
		args = &OrganizationArgs{}
	}

	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Organization
	err := ctx.RegisterResource("aws-native:organizations:Organization", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetOrganization gets an existing Organization resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetOrganization(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *OrganizationState, opts ...pulumi.ResourceOption) (*Organization, error) {
	var resource Organization
	err := ctx.ReadResource("aws-native:organizations:Organization", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Organization resources.
type organizationState struct {
}

type OrganizationState struct {
}

func (OrganizationState) ElementType() reflect.Type {
	return reflect.TypeOf((*organizationState)(nil)).Elem()
}

type organizationArgs struct {
	// Specifies the feature set supported by the new organization. Each feature set supports different levels of functionality.
	FeatureSet *OrganizationFeatureSet `pulumi:"featureSet"`
}

// The set of arguments for constructing a Organization resource.
type OrganizationArgs struct {
	// Specifies the feature set supported by the new organization. Each feature set supports different levels of functionality.
	FeatureSet OrganizationFeatureSetPtrInput
}

func (OrganizationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*organizationArgs)(nil)).Elem()
}

type OrganizationInput interface {
	pulumi.Input

	ToOrganizationOutput() OrganizationOutput
	ToOrganizationOutputWithContext(ctx context.Context) OrganizationOutput
}

func (*Organization) ElementType() reflect.Type {
	return reflect.TypeOf((**Organization)(nil)).Elem()
}

func (i *Organization) ToOrganizationOutput() OrganizationOutput {
	return i.ToOrganizationOutputWithContext(context.Background())
}

func (i *Organization) ToOrganizationOutputWithContext(ctx context.Context) OrganizationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OrganizationOutput)
}

func (i *Organization) ToOutput(ctx context.Context) pulumix.Output[*Organization] {
	return pulumix.Output[*Organization]{
		OutputState: i.ToOrganizationOutputWithContext(ctx).OutputState,
	}
}

type OrganizationOutput struct{ *pulumi.OutputState }

func (OrganizationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Organization)(nil)).Elem()
}

func (o OrganizationOutput) ToOrganizationOutput() OrganizationOutput {
	return o
}

func (o OrganizationOutput) ToOrganizationOutputWithContext(ctx context.Context) OrganizationOutput {
	return o
}

func (o OrganizationOutput) ToOutput(ctx context.Context) pulumix.Output[*Organization] {
	return pulumix.Output[*Organization]{
		OutputState: o.OutputState,
	}
}

// The Amazon Resource Name (ARN) of an organization.
func (o OrganizationOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *Organization) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

// Specifies the feature set supported by the new organization. Each feature set supports different levels of functionality.
func (o OrganizationOutput) FeatureSet() OrganizationFeatureSetPtrOutput {
	return o.ApplyT(func(v *Organization) OrganizationFeatureSetPtrOutput { return v.FeatureSet }).(OrganizationFeatureSetPtrOutput)
}

// The Amazon Resource Name (ARN) of the account that is designated as the management account for the organization.
func (o OrganizationOutput) ManagementAccountArn() pulumi.StringOutput {
	return o.ApplyT(func(v *Organization) pulumi.StringOutput { return v.ManagementAccountArn }).(pulumi.StringOutput)
}

// The email address that is associated with the AWS account that is designated as the management account for the organization.
func (o OrganizationOutput) ManagementAccountEmail() pulumi.StringOutput {
	return o.ApplyT(func(v *Organization) pulumi.StringOutput { return v.ManagementAccountEmail }).(pulumi.StringOutput)
}

// The unique identifier (ID) of the management account of an organization.
func (o OrganizationOutput) ManagementAccountId() pulumi.StringOutput {
	return o.ApplyT(func(v *Organization) pulumi.StringOutput { return v.ManagementAccountId }).(pulumi.StringOutput)
}

// The unique identifier (ID) for the root.
func (o OrganizationOutput) RootId() pulumi.StringOutput {
	return o.ApplyT(func(v *Organization) pulumi.StringOutput { return v.RootId }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*OrganizationInput)(nil)).Elem(), &Organization{})
	pulumi.RegisterOutputType(OrganizationOutput{})
}
