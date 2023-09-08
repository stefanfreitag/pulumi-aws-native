// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package gamelift

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::GameLift::Build
func LookupBuild(ctx *pulumi.Context, args *LookupBuildArgs, opts ...pulumi.InvokeOption) (*LookupBuildResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupBuildResult
	err := ctx.Invoke("aws-native:gamelift:getBuild", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupBuildArgs struct {
	// A unique identifier for a build to be deployed on the new fleet. If you are deploying the fleet with a custom game build, you must specify this property. The build must have been successfully uploaded to Amazon GameLift and be in a READY status. This fleet setting cannot be changed once the fleet is created.
	BuildId string `pulumi:"buildId"`
}

type LookupBuildResult struct {
	// A unique identifier for a build to be deployed on the new fleet. If you are deploying the fleet with a custom game build, you must specify this property. The build must have been successfully uploaded to Amazon GameLift and be in a READY status. This fleet setting cannot be changed once the fleet is created.
	BuildId *string `pulumi:"buildId"`
	// A descriptive label that is associated with a build. Build names do not need to be unique.
	Name *string `pulumi:"name"`
	// Version information that is associated with this build. Version strings do not need to be unique.
	Version *string `pulumi:"version"`
}

func LookupBuildOutput(ctx *pulumi.Context, args LookupBuildOutputArgs, opts ...pulumi.InvokeOption) LookupBuildResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupBuildResult, error) {
			args := v.(LookupBuildArgs)
			r, err := LookupBuild(ctx, &args, opts...)
			var s LookupBuildResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupBuildResultOutput)
}

type LookupBuildOutputArgs struct {
	// A unique identifier for a build to be deployed on the new fleet. If you are deploying the fleet with a custom game build, you must specify this property. The build must have been successfully uploaded to Amazon GameLift and be in a READY status. This fleet setting cannot be changed once the fleet is created.
	BuildId pulumi.StringInput `pulumi:"buildId"`
}

func (LookupBuildOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupBuildArgs)(nil)).Elem()
}

type LookupBuildResultOutput struct{ *pulumi.OutputState }

func (LookupBuildResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupBuildResult)(nil)).Elem()
}

func (o LookupBuildResultOutput) ToLookupBuildResultOutput() LookupBuildResultOutput {
	return o
}

func (o LookupBuildResultOutput) ToLookupBuildResultOutputWithContext(ctx context.Context) LookupBuildResultOutput {
	return o
}

func (o LookupBuildResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupBuildResult] {
	return pulumix.Output[LookupBuildResult]{
		OutputState: o.OutputState,
	}
}

// A unique identifier for a build to be deployed on the new fleet. If you are deploying the fleet with a custom game build, you must specify this property. The build must have been successfully uploaded to Amazon GameLift and be in a READY status. This fleet setting cannot be changed once the fleet is created.
func (o LookupBuildResultOutput) BuildId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupBuildResult) *string { return v.BuildId }).(pulumi.StringPtrOutput)
}

// A descriptive label that is associated with a build. Build names do not need to be unique.
func (o LookupBuildResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupBuildResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

// Version information that is associated with this build. Version strings do not need to be unique.
func (o LookupBuildResultOutput) Version() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupBuildResult) *string { return v.Version }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupBuildResultOutput{})
}
