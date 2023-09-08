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

// Resource Type definition for AWS::Config::ConfigurationAggregator
func LookupConfigurationAggregator(ctx *pulumi.Context, args *LookupConfigurationAggregatorArgs, opts ...pulumi.InvokeOption) (*LookupConfigurationAggregatorResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupConfigurationAggregatorResult
	err := ctx.Invoke("aws-native:configuration:getConfigurationAggregator", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupConfigurationAggregatorArgs struct {
	// The name of the aggregator.
	ConfigurationAggregatorName string `pulumi:"configurationAggregatorName"`
}

type LookupConfigurationAggregatorResult struct {
	AccountAggregationSources []ConfigurationAggregatorAccountAggregationSource `pulumi:"accountAggregationSources"`
	// The Amazon Resource Name (ARN) of the aggregator.
	ConfigurationAggregatorArn    *string                                               `pulumi:"configurationAggregatorArn"`
	OrganizationAggregationSource *ConfigurationAggregatorOrganizationAggregationSource `pulumi:"organizationAggregationSource"`
	// The tags for the configuration aggregator.
	Tags []ConfigurationAggregatorTag `pulumi:"tags"`
}

func LookupConfigurationAggregatorOutput(ctx *pulumi.Context, args LookupConfigurationAggregatorOutputArgs, opts ...pulumi.InvokeOption) LookupConfigurationAggregatorResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupConfigurationAggregatorResult, error) {
			args := v.(LookupConfigurationAggregatorArgs)
			r, err := LookupConfigurationAggregator(ctx, &args, opts...)
			var s LookupConfigurationAggregatorResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupConfigurationAggregatorResultOutput)
}

type LookupConfigurationAggregatorOutputArgs struct {
	// The name of the aggregator.
	ConfigurationAggregatorName pulumi.StringInput `pulumi:"configurationAggregatorName"`
}

func (LookupConfigurationAggregatorOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupConfigurationAggregatorArgs)(nil)).Elem()
}

type LookupConfigurationAggregatorResultOutput struct{ *pulumi.OutputState }

func (LookupConfigurationAggregatorResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupConfigurationAggregatorResult)(nil)).Elem()
}

func (o LookupConfigurationAggregatorResultOutput) ToLookupConfigurationAggregatorResultOutput() LookupConfigurationAggregatorResultOutput {
	return o
}

func (o LookupConfigurationAggregatorResultOutput) ToLookupConfigurationAggregatorResultOutputWithContext(ctx context.Context) LookupConfigurationAggregatorResultOutput {
	return o
}

func (o LookupConfigurationAggregatorResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupConfigurationAggregatorResult] {
	return pulumix.Output[LookupConfigurationAggregatorResult]{
		OutputState: o.OutputState,
	}
}

func (o LookupConfigurationAggregatorResultOutput) AccountAggregationSources() ConfigurationAggregatorAccountAggregationSourceArrayOutput {
	return o.ApplyT(func(v LookupConfigurationAggregatorResult) []ConfigurationAggregatorAccountAggregationSource {
		return v.AccountAggregationSources
	}).(ConfigurationAggregatorAccountAggregationSourceArrayOutput)
}

// The Amazon Resource Name (ARN) of the aggregator.
func (o LookupConfigurationAggregatorResultOutput) ConfigurationAggregatorArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupConfigurationAggregatorResult) *string { return v.ConfigurationAggregatorArn }).(pulumi.StringPtrOutput)
}

func (o LookupConfigurationAggregatorResultOutput) OrganizationAggregationSource() ConfigurationAggregatorOrganizationAggregationSourcePtrOutput {
	return o.ApplyT(func(v LookupConfigurationAggregatorResult) *ConfigurationAggregatorOrganizationAggregationSource {
		return v.OrganizationAggregationSource
	}).(ConfigurationAggregatorOrganizationAggregationSourcePtrOutput)
}

// The tags for the configuration aggregator.
func (o LookupConfigurationAggregatorResultOutput) Tags() ConfigurationAggregatorTagArrayOutput {
	return o.ApplyT(func(v LookupConfigurationAggregatorResult) []ConfigurationAggregatorTag { return v.Tags }).(ConfigurationAggregatorTagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupConfigurationAggregatorResultOutput{})
}
