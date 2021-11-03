// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package iot

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Configures the Device Defender audit settings for this account. Settings include how audit notifications are sent and which audit checks are enabled or disabled.
type AccountAuditConfiguration struct {
	pulumi.CustomResourceState

	// Your 12-digit account ID (used as the primary identifier for the CloudFormation resource).
	AccountId                             pulumi.StringOutput                                                     `pulumi:"accountId"`
	AuditCheckConfigurations              AccountAuditConfigurationAuditCheckConfigurationsOutput                 `pulumi:"auditCheckConfigurations"`
	AuditNotificationTargetConfigurations AccountAuditConfigurationAuditNotificationTargetConfigurationsPtrOutput `pulumi:"auditNotificationTargetConfigurations"`
	// The ARN of the role that grants permission to AWS IoT to access information about your devices, policies, certificates and other items as required when performing an audit.
	RoleArn pulumi.StringOutput `pulumi:"roleArn"`
}

// NewAccountAuditConfiguration registers a new resource with the given unique name, arguments, and options.
func NewAccountAuditConfiguration(ctx *pulumi.Context,
	name string, args *AccountAuditConfigurationArgs, opts ...pulumi.ResourceOption) (*AccountAuditConfiguration, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.AccountId == nil {
		return nil, errors.New("invalid value for required argument 'AccountId'")
	}
	if args.AuditCheckConfigurations == nil {
		return nil, errors.New("invalid value for required argument 'AuditCheckConfigurations'")
	}
	if args.RoleArn == nil {
		return nil, errors.New("invalid value for required argument 'RoleArn'")
	}
	var resource AccountAuditConfiguration
	err := ctx.RegisterResource("aws-native:iot:AccountAuditConfiguration", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetAccountAuditConfiguration gets an existing AccountAuditConfiguration resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetAccountAuditConfiguration(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *AccountAuditConfigurationState, opts ...pulumi.ResourceOption) (*AccountAuditConfiguration, error) {
	var resource AccountAuditConfiguration
	err := ctx.ReadResource("aws-native:iot:AccountAuditConfiguration", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering AccountAuditConfiguration resources.
type accountAuditConfigurationState struct {
}

type AccountAuditConfigurationState struct {
}

func (AccountAuditConfigurationState) ElementType() reflect.Type {
	return reflect.TypeOf((*accountAuditConfigurationState)(nil)).Elem()
}

type accountAuditConfigurationArgs struct {
	// Your 12-digit account ID (used as the primary identifier for the CloudFormation resource).
	AccountId                             string                                                          `pulumi:"accountId"`
	AuditCheckConfigurations              AccountAuditConfigurationAuditCheckConfigurations               `pulumi:"auditCheckConfigurations"`
	AuditNotificationTargetConfigurations *AccountAuditConfigurationAuditNotificationTargetConfigurations `pulumi:"auditNotificationTargetConfigurations"`
	// The ARN of the role that grants permission to AWS IoT to access information about your devices, policies, certificates and other items as required when performing an audit.
	RoleArn string `pulumi:"roleArn"`
}

// The set of arguments for constructing a AccountAuditConfiguration resource.
type AccountAuditConfigurationArgs struct {
	// Your 12-digit account ID (used as the primary identifier for the CloudFormation resource).
	AccountId                             pulumi.StringInput
	AuditCheckConfigurations              AccountAuditConfigurationAuditCheckConfigurationsInput
	AuditNotificationTargetConfigurations AccountAuditConfigurationAuditNotificationTargetConfigurationsPtrInput
	// The ARN of the role that grants permission to AWS IoT to access information about your devices, policies, certificates and other items as required when performing an audit.
	RoleArn pulumi.StringInput
}

func (AccountAuditConfigurationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*accountAuditConfigurationArgs)(nil)).Elem()
}

type AccountAuditConfigurationInput interface {
	pulumi.Input

	ToAccountAuditConfigurationOutput() AccountAuditConfigurationOutput
	ToAccountAuditConfigurationOutputWithContext(ctx context.Context) AccountAuditConfigurationOutput
}

func (*AccountAuditConfiguration) ElementType() reflect.Type {
	return reflect.TypeOf((*AccountAuditConfiguration)(nil))
}

func (i *AccountAuditConfiguration) ToAccountAuditConfigurationOutput() AccountAuditConfigurationOutput {
	return i.ToAccountAuditConfigurationOutputWithContext(context.Background())
}

func (i *AccountAuditConfiguration) ToAccountAuditConfigurationOutputWithContext(ctx context.Context) AccountAuditConfigurationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AccountAuditConfigurationOutput)
}

type AccountAuditConfigurationOutput struct{ *pulumi.OutputState }

func (AccountAuditConfigurationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*AccountAuditConfiguration)(nil))
}

func (o AccountAuditConfigurationOutput) ToAccountAuditConfigurationOutput() AccountAuditConfigurationOutput {
	return o
}

func (o AccountAuditConfigurationOutput) ToAccountAuditConfigurationOutputWithContext(ctx context.Context) AccountAuditConfigurationOutput {
	return o
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*AccountAuditConfigurationInput)(nil)).Elem(), &AccountAuditConfiguration{})
	pulumi.RegisterOutputType(AccountAuditConfigurationOutput{})
}
