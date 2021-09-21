// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package configuration

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::Config::OrganizationConfigRule
//
// Deprecated: OrganizationConfigRule is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
type OrganizationConfigRule struct {
	pulumi.CustomResourceState

	ExcludedAccounts                pulumi.StringArrayOutput                                       `pulumi:"excludedAccounts"`
	OrganizationConfigRuleName      pulumi.StringOutput                                            `pulumi:"organizationConfigRuleName"`
	OrganizationCustomRuleMetadata  OrganizationConfigRuleOrganizationCustomRuleMetadataPtrOutput  `pulumi:"organizationCustomRuleMetadata"`
	OrganizationManagedRuleMetadata OrganizationConfigRuleOrganizationManagedRuleMetadataPtrOutput `pulumi:"organizationManagedRuleMetadata"`
}

// NewOrganizationConfigRule registers a new resource with the given unique name, arguments, and options.
func NewOrganizationConfigRule(ctx *pulumi.Context,
	name string, args *OrganizationConfigRuleArgs, opts ...pulumi.ResourceOption) (*OrganizationConfigRule, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.OrganizationConfigRuleName == nil {
		return nil, errors.New("invalid value for required argument 'OrganizationConfigRuleName'")
	}
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
	ExcludedAccounts                []string                                               `pulumi:"excludedAccounts"`
	OrganizationConfigRuleName      string                                                 `pulumi:"organizationConfigRuleName"`
	OrganizationCustomRuleMetadata  *OrganizationConfigRuleOrganizationCustomRuleMetadata  `pulumi:"organizationCustomRuleMetadata"`
	OrganizationManagedRuleMetadata *OrganizationConfigRuleOrganizationManagedRuleMetadata `pulumi:"organizationManagedRuleMetadata"`
}

// The set of arguments for constructing a OrganizationConfigRule resource.
type OrganizationConfigRuleArgs struct {
	ExcludedAccounts                pulumi.StringArrayInput
	OrganizationConfigRuleName      pulumi.StringInput
	OrganizationCustomRuleMetadata  OrganizationConfigRuleOrganizationCustomRuleMetadataPtrInput
	OrganizationManagedRuleMetadata OrganizationConfigRuleOrganizationManagedRuleMetadataPtrInput
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
	return reflect.TypeOf((*OrganizationConfigRule)(nil))
}

func (i *OrganizationConfigRule) ToOrganizationConfigRuleOutput() OrganizationConfigRuleOutput {
	return i.ToOrganizationConfigRuleOutputWithContext(context.Background())
}

func (i *OrganizationConfigRule) ToOrganizationConfigRuleOutputWithContext(ctx context.Context) OrganizationConfigRuleOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OrganizationConfigRuleOutput)
}

type OrganizationConfigRuleOutput struct{ *pulumi.OutputState }

func (OrganizationConfigRuleOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*OrganizationConfigRule)(nil))
}

func (o OrganizationConfigRuleOutput) ToOrganizationConfigRuleOutput() OrganizationConfigRuleOutput {
	return o
}

func (o OrganizationConfigRuleOutput) ToOrganizationConfigRuleOutputWithContext(ctx context.Context) OrganizationConfigRuleOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(OrganizationConfigRuleOutput{})
}
