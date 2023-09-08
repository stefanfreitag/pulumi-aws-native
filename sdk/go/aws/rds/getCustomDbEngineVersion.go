// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package rds

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// The AWS::RDS::CustomDBEngineVersion resource creates an Amazon RDS custom DB engine version.
func LookupCustomDbEngineVersion(ctx *pulumi.Context, args *LookupCustomDbEngineVersionArgs, opts ...pulumi.InvokeOption) (*LookupCustomDbEngineVersionResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupCustomDbEngineVersionResult
	err := ctx.Invoke("aws-native:rds:getCustomDbEngineVersion", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupCustomDbEngineVersionArgs struct {
	// The database engine to use for your custom engine version (CEV). The only supported value is `custom-oracle-ee`.
	Engine string `pulumi:"engine"`
	// The name of your CEV. The name format is 19.customized_string . For example, a valid name is 19.my_cev1. This setting is required for RDS Custom for Oracle, but optional for Amazon RDS. The combination of Engine and EngineVersion is unique per customer per Region.
	EngineVersion string `pulumi:"engineVersion"`
}

type LookupCustomDbEngineVersionResult struct {
	// The ARN of the custom engine version.
	DbEngineVersionArn *string `pulumi:"dbEngineVersionArn"`
	// An optional description of your CEV.
	Description *string `pulumi:"description"`
	// The availability status to be assigned to the CEV.
	Status *CustomDbEngineVersionStatus `pulumi:"status"`
	// An array of key-value pairs to apply to this resource.
	Tags []CustomDbEngineVersionTag `pulumi:"tags"`
}

func LookupCustomDbEngineVersionOutput(ctx *pulumi.Context, args LookupCustomDbEngineVersionOutputArgs, opts ...pulumi.InvokeOption) LookupCustomDbEngineVersionResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupCustomDbEngineVersionResult, error) {
			args := v.(LookupCustomDbEngineVersionArgs)
			r, err := LookupCustomDbEngineVersion(ctx, &args, opts...)
			var s LookupCustomDbEngineVersionResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupCustomDbEngineVersionResultOutput)
}

type LookupCustomDbEngineVersionOutputArgs struct {
	// The database engine to use for your custom engine version (CEV). The only supported value is `custom-oracle-ee`.
	Engine pulumi.StringInput `pulumi:"engine"`
	// The name of your CEV. The name format is 19.customized_string . For example, a valid name is 19.my_cev1. This setting is required for RDS Custom for Oracle, but optional for Amazon RDS. The combination of Engine and EngineVersion is unique per customer per Region.
	EngineVersion pulumi.StringInput `pulumi:"engineVersion"`
}

func (LookupCustomDbEngineVersionOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupCustomDbEngineVersionArgs)(nil)).Elem()
}

type LookupCustomDbEngineVersionResultOutput struct{ *pulumi.OutputState }

func (LookupCustomDbEngineVersionResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupCustomDbEngineVersionResult)(nil)).Elem()
}

func (o LookupCustomDbEngineVersionResultOutput) ToLookupCustomDbEngineVersionResultOutput() LookupCustomDbEngineVersionResultOutput {
	return o
}

func (o LookupCustomDbEngineVersionResultOutput) ToLookupCustomDbEngineVersionResultOutputWithContext(ctx context.Context) LookupCustomDbEngineVersionResultOutput {
	return o
}

func (o LookupCustomDbEngineVersionResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupCustomDbEngineVersionResult] {
	return pulumix.Output[LookupCustomDbEngineVersionResult]{
		OutputState: o.OutputState,
	}
}

// The ARN of the custom engine version.
func (o LookupCustomDbEngineVersionResultOutput) DbEngineVersionArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupCustomDbEngineVersionResult) *string { return v.DbEngineVersionArn }).(pulumi.StringPtrOutput)
}

// An optional description of your CEV.
func (o LookupCustomDbEngineVersionResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupCustomDbEngineVersionResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

// The availability status to be assigned to the CEV.
func (o LookupCustomDbEngineVersionResultOutput) Status() CustomDbEngineVersionStatusPtrOutput {
	return o.ApplyT(func(v LookupCustomDbEngineVersionResult) *CustomDbEngineVersionStatus { return v.Status }).(CustomDbEngineVersionStatusPtrOutput)
}

// An array of key-value pairs to apply to this resource.
func (o LookupCustomDbEngineVersionResultOutput) Tags() CustomDbEngineVersionTagArrayOutput {
	return o.ApplyT(func(v LookupCustomDbEngineVersionResult) []CustomDbEngineVersionTag { return v.Tags }).(CustomDbEngineVersionTagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupCustomDbEngineVersionResultOutput{})
}
