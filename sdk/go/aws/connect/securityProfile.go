// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package connect

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::Connect::SecurityProfile
type SecurityProfile struct {
	pulumi.CustomResourceState

	// The list of tags that a security profile uses to restrict access to resources in Amazon Connect.
	AllowedAccessControlTags SecurityProfileTagArrayOutput `pulumi:"allowedAccessControlTags"`
	// The description of the security profile.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The identifier of the Amazon Connect instance.
	InstanceArn pulumi.StringOutput `pulumi:"instanceArn"`
	// Permissions assigned to the security profile.
	Permissions pulumi.StringArrayOutput `pulumi:"permissions"`
	// The Amazon Resource Name (ARN) for the security profile.
	SecurityProfileArn pulumi.StringOutput `pulumi:"securityProfileArn"`
	// The name of the security profile.
	SecurityProfileName pulumi.StringOutput `pulumi:"securityProfileName"`
	// The list of resources that a security profile applies tag restrictions to in Amazon Connect.
	TagRestrictedResources pulumi.StringArrayOutput `pulumi:"tagRestrictedResources"`
	// The tags used to organize, track, or control access for this resource.
	Tags SecurityProfileTagArrayOutput `pulumi:"tags"`
}

// NewSecurityProfile registers a new resource with the given unique name, arguments, and options.
func NewSecurityProfile(ctx *pulumi.Context,
	name string, args *SecurityProfileArgs, opts ...pulumi.ResourceOption) (*SecurityProfile, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.InstanceArn == nil {
		return nil, errors.New("invalid value for required argument 'InstanceArn'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"instanceArn",
		"securityProfileName",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource SecurityProfile
	err := ctx.RegisterResource("aws-native:connect:SecurityProfile", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSecurityProfile gets an existing SecurityProfile resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSecurityProfile(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SecurityProfileState, opts ...pulumi.ResourceOption) (*SecurityProfile, error) {
	var resource SecurityProfile
	err := ctx.ReadResource("aws-native:connect:SecurityProfile", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering SecurityProfile resources.
type securityProfileState struct {
}

type SecurityProfileState struct {
}

func (SecurityProfileState) ElementType() reflect.Type {
	return reflect.TypeOf((*securityProfileState)(nil)).Elem()
}

type securityProfileArgs struct {
	// The list of tags that a security profile uses to restrict access to resources in Amazon Connect.
	AllowedAccessControlTags []SecurityProfileTag `pulumi:"allowedAccessControlTags"`
	// The description of the security profile.
	Description *string `pulumi:"description"`
	// The identifier of the Amazon Connect instance.
	InstanceArn string `pulumi:"instanceArn"`
	// Permissions assigned to the security profile.
	Permissions []string `pulumi:"permissions"`
	// The name of the security profile.
	SecurityProfileName *string `pulumi:"securityProfileName"`
	// The list of resources that a security profile applies tag restrictions to in Amazon Connect.
	TagRestrictedResources []string `pulumi:"tagRestrictedResources"`
	// The tags used to organize, track, or control access for this resource.
	Tags []SecurityProfileTag `pulumi:"tags"`
}

// The set of arguments for constructing a SecurityProfile resource.
type SecurityProfileArgs struct {
	// The list of tags that a security profile uses to restrict access to resources in Amazon Connect.
	AllowedAccessControlTags SecurityProfileTagArrayInput
	// The description of the security profile.
	Description pulumi.StringPtrInput
	// The identifier of the Amazon Connect instance.
	InstanceArn pulumi.StringInput
	// Permissions assigned to the security profile.
	Permissions pulumi.StringArrayInput
	// The name of the security profile.
	SecurityProfileName pulumi.StringPtrInput
	// The list of resources that a security profile applies tag restrictions to in Amazon Connect.
	TagRestrictedResources pulumi.StringArrayInput
	// The tags used to organize, track, or control access for this resource.
	Tags SecurityProfileTagArrayInput
}

func (SecurityProfileArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*securityProfileArgs)(nil)).Elem()
}

type SecurityProfileInput interface {
	pulumi.Input

	ToSecurityProfileOutput() SecurityProfileOutput
	ToSecurityProfileOutputWithContext(ctx context.Context) SecurityProfileOutput
}

func (*SecurityProfile) ElementType() reflect.Type {
	return reflect.TypeOf((**SecurityProfile)(nil)).Elem()
}

func (i *SecurityProfile) ToSecurityProfileOutput() SecurityProfileOutput {
	return i.ToSecurityProfileOutputWithContext(context.Background())
}

func (i *SecurityProfile) ToSecurityProfileOutputWithContext(ctx context.Context) SecurityProfileOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SecurityProfileOutput)
}

func (i *SecurityProfile) ToOutput(ctx context.Context) pulumix.Output[*SecurityProfile] {
	return pulumix.Output[*SecurityProfile]{
		OutputState: i.ToSecurityProfileOutputWithContext(ctx).OutputState,
	}
}

type SecurityProfileOutput struct{ *pulumi.OutputState }

func (SecurityProfileOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**SecurityProfile)(nil)).Elem()
}

func (o SecurityProfileOutput) ToSecurityProfileOutput() SecurityProfileOutput {
	return o
}

func (o SecurityProfileOutput) ToSecurityProfileOutputWithContext(ctx context.Context) SecurityProfileOutput {
	return o
}

func (o SecurityProfileOutput) ToOutput(ctx context.Context) pulumix.Output[*SecurityProfile] {
	return pulumix.Output[*SecurityProfile]{
		OutputState: o.OutputState,
	}
}

// The list of tags that a security profile uses to restrict access to resources in Amazon Connect.
func (o SecurityProfileOutput) AllowedAccessControlTags() SecurityProfileTagArrayOutput {
	return o.ApplyT(func(v *SecurityProfile) SecurityProfileTagArrayOutput { return v.AllowedAccessControlTags }).(SecurityProfileTagArrayOutput)
}

// The description of the security profile.
func (o SecurityProfileOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *SecurityProfile) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// The identifier of the Amazon Connect instance.
func (o SecurityProfileOutput) InstanceArn() pulumi.StringOutput {
	return o.ApplyT(func(v *SecurityProfile) pulumi.StringOutput { return v.InstanceArn }).(pulumi.StringOutput)
}

// Permissions assigned to the security profile.
func (o SecurityProfileOutput) Permissions() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *SecurityProfile) pulumi.StringArrayOutput { return v.Permissions }).(pulumi.StringArrayOutput)
}

// The Amazon Resource Name (ARN) for the security profile.
func (o SecurityProfileOutput) SecurityProfileArn() pulumi.StringOutput {
	return o.ApplyT(func(v *SecurityProfile) pulumi.StringOutput { return v.SecurityProfileArn }).(pulumi.StringOutput)
}

// The name of the security profile.
func (o SecurityProfileOutput) SecurityProfileName() pulumi.StringOutput {
	return o.ApplyT(func(v *SecurityProfile) pulumi.StringOutput { return v.SecurityProfileName }).(pulumi.StringOutput)
}

// The list of resources that a security profile applies tag restrictions to in Amazon Connect.
func (o SecurityProfileOutput) TagRestrictedResources() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *SecurityProfile) pulumi.StringArrayOutput { return v.TagRestrictedResources }).(pulumi.StringArrayOutput)
}

// The tags used to organize, track, or control access for this resource.
func (o SecurityProfileOutput) Tags() SecurityProfileTagArrayOutput {
	return o.ApplyT(func(v *SecurityProfile) SecurityProfileTagArrayOutput { return v.Tags }).(SecurityProfileTagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*SecurityProfileInput)(nil)).Elem(), &SecurityProfile{})
	pulumi.RegisterOutputType(SecurityProfileOutput{})
}
