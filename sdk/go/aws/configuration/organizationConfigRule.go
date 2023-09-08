// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package configuration

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::Config::OrganizationConfigRule
//
// Deprecated: OrganizationConfigRule is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type OrganizationConfigRule struct {
	pulumi.CustomResourceState

	ExcludedAccounts                     pulumi.StringArrayOutput                                            `pulumi:"excludedAccounts"`
	OrganizationConfigRuleName           pulumi.StringOutput                                                 `pulumi:"organizationConfigRuleName"`
	OrganizationCustomPolicyRuleMetadata OrganizationConfigRuleOrganizationCustomPolicyRuleMetadataPtrOutput `pulumi:"organizationCustomPolicyRuleMetadata"`
	OrganizationCustomRuleMetadata       OrganizationConfigRuleOrganizationCustomRuleMetadataPtrOutput       `pulumi:"organizationCustomRuleMetadata"`
	OrganizationManagedRuleMetadata      OrganizationConfigRuleOrganizationManagedRuleMetadataPtrOutput      `pulumi:"organizationManagedRuleMetadata"`
}

// NewOrganizationConfigRule registers a new resource with the given unique name, arguments, and options.
func NewOrganizationConfigRule(ctx *pulumi.Context,
	name string, args *OrganizationConfigRuleArgs, opts ...pulumi.ResourceOption) (*OrganizationConfigRule, error) {
	if args == nil {
		args = &OrganizationConfigRuleArgs{}
	}

	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"organizationConfigRuleName",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource OrganizationConfigRule
	err := ctx.RegisterResource("aws-native:configuration:OrganizationConfigRule", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetOrganizationConfigRule gets an existing OrganizationConfigRule resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetOrganizationConfigRule(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *OrganizationConfigRuleState, opts ...pulumi.ResourceOption) (*OrganizationConfigRule, error) {
	var resource OrganizationConfigRule
	err := ctx.ReadResource("aws-native:configuration:OrganizationConfigRule", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering OrganizationConfigRule resources.
type organizationConfigRuleState struct {
}

type OrganizationConfigRuleState struct {
}

func (OrganizationConfigRuleState) ElementType() reflect.Type {
	return reflect.TypeOf((*organizationConfigRuleState)(nil)).Elem()
}

type organizationConfigRuleArgs struct {
	ExcludedAccounts                     []string                                                    `pulumi:"excludedAccounts"`
	OrganizationConfigRuleName           *string                                                     `pulumi:"organizationConfigRuleName"`
	OrganizationCustomPolicyRuleMetadata *OrganizationConfigRuleOrganizationCustomPolicyRuleMetadata `pulumi:"organizationCustomPolicyRuleMetadata"`
	OrganizationCustomRuleMetadata       *OrganizationConfigRuleOrganizationCustomRuleMetadata       `pulumi:"organizationCustomRuleMetadata"`
	OrganizationManagedRuleMetadata      *OrganizationConfigRuleOrganizationManagedRuleMetadata      `pulumi:"organizationManagedRuleMetadata"`
}

// The set of arguments for constructing a OrganizationConfigRule resource.
type OrganizationConfigRuleArgs struct {
	ExcludedAccounts                     pulumi.StringArrayInput
	OrganizationConfigRuleName           pulumi.StringPtrInput
	OrganizationCustomPolicyRuleMetadata OrganizationConfigRuleOrganizationCustomPolicyRuleMetadataPtrInput
	OrganizationCustomRuleMetadata       OrganizationConfigRuleOrganizationCustomRuleMetadataPtrInput
	OrganizationManagedRuleMetadata      OrganizationConfigRuleOrganizationManagedRuleMetadataPtrInput
}

func (OrganizationConfigRuleArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*organizationConfigRuleArgs)(nil)).Elem()
}

type OrganizationConfigRuleInput interface {
	pulumi.Input

	ToOrganizationConfigRuleOutput() OrganizationConfigRuleOutput
	ToOrganizationConfigRuleOutputWithContext(ctx context.Context) OrganizationConfigRuleOutput
}

func (*OrganizationConfigRule) ElementType() reflect.Type {
	return reflect.TypeOf((**OrganizationConfigRule)(nil)).Elem()
}

func (i *OrganizationConfigRule) ToOrganizationConfigRuleOutput() OrganizationConfigRuleOutput {
	return i.ToOrganizationConfigRuleOutputWithContext(context.Background())
}

func (i *OrganizationConfigRule) ToOrganizationConfigRuleOutputWithContext(ctx context.Context) OrganizationConfigRuleOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OrganizationConfigRuleOutput)
}

func (i *OrganizationConfigRule) ToOutput(ctx context.Context) pulumix.Output[*OrganizationConfigRule] {
	return pulumix.Output[*OrganizationConfigRule]{
		OutputState: i.ToOrganizationConfigRuleOutputWithContext(ctx).OutputState,
	}
}

type OrganizationConfigRuleOutput struct{ *pulumi.OutputState }

func (OrganizationConfigRuleOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**OrganizationConfigRule)(nil)).Elem()
}

func (o OrganizationConfigRuleOutput) ToOrganizationConfigRuleOutput() OrganizationConfigRuleOutput {
	return o
}

func (o OrganizationConfigRuleOutput) ToOrganizationConfigRuleOutputWithContext(ctx context.Context) OrganizationConfigRuleOutput {
	return o
}

func (o OrganizationConfigRuleOutput) ToOutput(ctx context.Context) pulumix.Output[*OrganizationConfigRule] {
	return pulumix.Output[*OrganizationConfigRule]{
		OutputState: o.OutputState,
	}
}

func (o OrganizationConfigRuleOutput) ExcludedAccounts() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *OrganizationConfigRule) pulumi.StringArrayOutput { return v.ExcludedAccounts }).(pulumi.StringArrayOutput)
}

func (o OrganizationConfigRuleOutput) OrganizationConfigRuleName() pulumi.StringOutput {
	return o.ApplyT(func(v *OrganizationConfigRule) pulumi.StringOutput { return v.OrganizationConfigRuleName }).(pulumi.StringOutput)
}

func (o OrganizationConfigRuleOutput) OrganizationCustomPolicyRuleMetadata() OrganizationConfigRuleOrganizationCustomPolicyRuleMetadataPtrOutput {
	return o.ApplyT(func(v *OrganizationConfigRule) OrganizationConfigRuleOrganizationCustomPolicyRuleMetadataPtrOutput {
		return v.OrganizationCustomPolicyRuleMetadata
	}).(OrganizationConfigRuleOrganizationCustomPolicyRuleMetadataPtrOutput)
}

func (o OrganizationConfigRuleOutput) OrganizationCustomRuleMetadata() OrganizationConfigRuleOrganizationCustomRuleMetadataPtrOutput {
	return o.ApplyT(func(v *OrganizationConfigRule) OrganizationConfigRuleOrganizationCustomRuleMetadataPtrOutput {
		return v.OrganizationCustomRuleMetadata
	}).(OrganizationConfigRuleOrganizationCustomRuleMetadataPtrOutput)
}

func (o OrganizationConfigRuleOutput) OrganizationManagedRuleMetadata() OrganizationConfigRuleOrganizationManagedRuleMetadataPtrOutput {
	return o.ApplyT(func(v *OrganizationConfigRule) OrganizationConfigRuleOrganizationManagedRuleMetadataPtrOutput {
		return v.OrganizationManagedRuleMetadata
	}).(OrganizationConfigRuleOrganizationManagedRuleMetadataPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*OrganizationConfigRuleInput)(nil)).Elem(), &OrganizationConfigRule{})
	pulumi.RegisterOutputType(OrganizationConfigRuleOutput{})
}
