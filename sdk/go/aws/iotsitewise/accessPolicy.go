// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package iotsitewise

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource schema for AWS::IoTSiteWise::AccessPolicy
type AccessPolicy struct {
	pulumi.CustomResourceState

	// The ARN of the access policy.
	AccessPolicyArn pulumi.StringOutput `pulumi:"accessPolicyArn"`
	// The ID of the access policy.
	AccessPolicyId pulumi.StringOutput `pulumi:"accessPolicyId"`
	// The identity for this access policy. Choose either a user or a group but not both.
	AccessPolicyIdentity AccessPolicyIdentityOutput `pulumi:"accessPolicyIdentity"`
	// The permission level for this access policy. Valid values are ADMINISTRATOR or VIEWER.
	AccessPolicyPermission pulumi.StringOutput `pulumi:"accessPolicyPermission"`
	// The AWS IoT SiteWise Monitor resource for this access policy. Choose either portal or project but not both.
	AccessPolicyResource AccessPolicyResourceOutput `pulumi:"accessPolicyResource"`
}

// NewAccessPolicy registers a new resource with the given unique name, arguments, and options.
func NewAccessPolicy(ctx *pulumi.Context,
	name string, args *AccessPolicyArgs, opts ...pulumi.ResourceOption) (*AccessPolicy, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.AccessPolicyIdentity == nil {
		return nil, errors.New("invalid value for required argument 'AccessPolicyIdentity'")
	}
	if args.AccessPolicyPermission == nil {
		return nil, errors.New("invalid value for required argument 'AccessPolicyPermission'")
	}
	if args.AccessPolicyResource == nil {
		return nil, errors.New("invalid value for required argument 'AccessPolicyResource'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource AccessPolicy
	err := ctx.RegisterResource("aws-native:iotsitewise:AccessPolicy", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetAccessPolicy gets an existing AccessPolicy resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetAccessPolicy(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *AccessPolicyState, opts ...pulumi.ResourceOption) (*AccessPolicy, error) {
	var resource AccessPolicy
	err := ctx.ReadResource("aws-native:iotsitewise:AccessPolicy", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering AccessPolicy resources.
type accessPolicyState struct {
}

type AccessPolicyState struct {
}

func (AccessPolicyState) ElementType() reflect.Type {
	return reflect.TypeOf((*accessPolicyState)(nil)).Elem()
}

type accessPolicyArgs struct {
	// The identity for this access policy. Choose either a user or a group but not both.
	AccessPolicyIdentity AccessPolicyIdentity `pulumi:"accessPolicyIdentity"`
	// The permission level for this access policy. Valid values are ADMINISTRATOR or VIEWER.
	AccessPolicyPermission string `pulumi:"accessPolicyPermission"`
	// The AWS IoT SiteWise Monitor resource for this access policy. Choose either portal or project but not both.
	AccessPolicyResource AccessPolicyResource `pulumi:"accessPolicyResource"`
}

// The set of arguments for constructing a AccessPolicy resource.
type AccessPolicyArgs struct {
	// The identity for this access policy. Choose either a user or a group but not both.
	AccessPolicyIdentity AccessPolicyIdentityInput
	// The permission level for this access policy. Valid values are ADMINISTRATOR or VIEWER.
	AccessPolicyPermission pulumi.StringInput
	// The AWS IoT SiteWise Monitor resource for this access policy. Choose either portal or project but not both.
	AccessPolicyResource AccessPolicyResourceInput
}

func (AccessPolicyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*accessPolicyArgs)(nil)).Elem()
}

type AccessPolicyInput interface {
	pulumi.Input

	ToAccessPolicyOutput() AccessPolicyOutput
	ToAccessPolicyOutputWithContext(ctx context.Context) AccessPolicyOutput
}

func (*AccessPolicy) ElementType() reflect.Type {
	return reflect.TypeOf((**AccessPolicy)(nil)).Elem()
}

func (i *AccessPolicy) ToAccessPolicyOutput() AccessPolicyOutput {
	return i.ToAccessPolicyOutputWithContext(context.Background())
}

func (i *AccessPolicy) ToAccessPolicyOutputWithContext(ctx context.Context) AccessPolicyOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AccessPolicyOutput)
}

func (i *AccessPolicy) ToOutput(ctx context.Context) pulumix.Output[*AccessPolicy] {
	return pulumix.Output[*AccessPolicy]{
		OutputState: i.ToAccessPolicyOutputWithContext(ctx).OutputState,
	}
}

type AccessPolicyOutput struct{ *pulumi.OutputState }

func (AccessPolicyOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**AccessPolicy)(nil)).Elem()
}

func (o AccessPolicyOutput) ToAccessPolicyOutput() AccessPolicyOutput {
	return o
}

func (o AccessPolicyOutput) ToAccessPolicyOutputWithContext(ctx context.Context) AccessPolicyOutput {
	return o
}

func (o AccessPolicyOutput) ToOutput(ctx context.Context) pulumix.Output[*AccessPolicy] {
	return pulumix.Output[*AccessPolicy]{
		OutputState: o.OutputState,
	}
}

// The ARN of the access policy.
func (o AccessPolicyOutput) AccessPolicyArn() pulumi.StringOutput {
	return o.ApplyT(func(v *AccessPolicy) pulumi.StringOutput { return v.AccessPolicyArn }).(pulumi.StringOutput)
}

// The ID of the access policy.
func (o AccessPolicyOutput) AccessPolicyId() pulumi.StringOutput {
	return o.ApplyT(func(v *AccessPolicy) pulumi.StringOutput { return v.AccessPolicyId }).(pulumi.StringOutput)
}

// The identity for this access policy. Choose either a user or a group but not both.
func (o AccessPolicyOutput) AccessPolicyIdentity() AccessPolicyIdentityOutput {
	return o.ApplyT(func(v *AccessPolicy) AccessPolicyIdentityOutput { return v.AccessPolicyIdentity }).(AccessPolicyIdentityOutput)
}

// The permission level for this access policy. Valid values are ADMINISTRATOR or VIEWER.
func (o AccessPolicyOutput) AccessPolicyPermission() pulumi.StringOutput {
	return o.ApplyT(func(v *AccessPolicy) pulumi.StringOutput { return v.AccessPolicyPermission }).(pulumi.StringOutput)
}

// The AWS IoT SiteWise Monitor resource for this access policy. Choose either portal or project but not both.
func (o AccessPolicyOutput) AccessPolicyResource() AccessPolicyResourceOutput {
	return o.ApplyT(func(v *AccessPolicy) AccessPolicyResourceOutput { return v.AccessPolicyResource }).(AccessPolicyResourceOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*AccessPolicyInput)(nil)).Elem(), &AccessPolicy{})
	pulumi.RegisterOutputType(AccessPolicyOutput{})
}
