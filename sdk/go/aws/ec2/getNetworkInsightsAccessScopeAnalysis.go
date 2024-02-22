// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ec2

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource schema for AWS::EC2::NetworkInsightsAccessScopeAnalysis
func LookupNetworkInsightsAccessScopeAnalysis(ctx *pulumi.Context, args *LookupNetworkInsightsAccessScopeAnalysisArgs, opts ...pulumi.InvokeOption) (*LookupNetworkInsightsAccessScopeAnalysisResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupNetworkInsightsAccessScopeAnalysisResult
	err := ctx.Invoke("aws-native:ec2:getNetworkInsightsAccessScopeAnalysis", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupNetworkInsightsAccessScopeAnalysisArgs struct {
	NetworkInsightsAccessScopeAnalysisId string `pulumi:"networkInsightsAccessScopeAnalysisId"`
}

type LookupNetworkInsightsAccessScopeAnalysisResult struct {
	AnalyzedEniCount                      *int                                             `pulumi:"analyzedEniCount"`
	EndDate                               *string                                          `pulumi:"endDate"`
	FindingsFound                         *NetworkInsightsAccessScopeAnalysisFindingsFound `pulumi:"findingsFound"`
	NetworkInsightsAccessScopeAnalysisArn *string                                          `pulumi:"networkInsightsAccessScopeAnalysisArn"`
	NetworkInsightsAccessScopeAnalysisId  *string                                          `pulumi:"networkInsightsAccessScopeAnalysisId"`
	StartDate                             *string                                          `pulumi:"startDate"`
	Status                                *NetworkInsightsAccessScopeAnalysisStatus        `pulumi:"status"`
	StatusMessage                         *string                                          `pulumi:"statusMessage"`
	Tags                                  []aws.Tag                                        `pulumi:"tags"`
}

func LookupNetworkInsightsAccessScopeAnalysisOutput(ctx *pulumi.Context, args LookupNetworkInsightsAccessScopeAnalysisOutputArgs, opts ...pulumi.InvokeOption) LookupNetworkInsightsAccessScopeAnalysisResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupNetworkInsightsAccessScopeAnalysisResult, error) {
			args := v.(LookupNetworkInsightsAccessScopeAnalysisArgs)
			r, err := LookupNetworkInsightsAccessScopeAnalysis(ctx, &args, opts...)
			var s LookupNetworkInsightsAccessScopeAnalysisResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupNetworkInsightsAccessScopeAnalysisResultOutput)
}

type LookupNetworkInsightsAccessScopeAnalysisOutputArgs struct {
	NetworkInsightsAccessScopeAnalysisId pulumi.StringInput `pulumi:"networkInsightsAccessScopeAnalysisId"`
}

func (LookupNetworkInsightsAccessScopeAnalysisOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupNetworkInsightsAccessScopeAnalysisArgs)(nil)).Elem()
}

type LookupNetworkInsightsAccessScopeAnalysisResultOutput struct{ *pulumi.OutputState }

func (LookupNetworkInsightsAccessScopeAnalysisResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupNetworkInsightsAccessScopeAnalysisResult)(nil)).Elem()
}

func (o LookupNetworkInsightsAccessScopeAnalysisResultOutput) ToLookupNetworkInsightsAccessScopeAnalysisResultOutput() LookupNetworkInsightsAccessScopeAnalysisResultOutput {
	return o
}

func (o LookupNetworkInsightsAccessScopeAnalysisResultOutput) ToLookupNetworkInsightsAccessScopeAnalysisResultOutputWithContext(ctx context.Context) LookupNetworkInsightsAccessScopeAnalysisResultOutput {
	return o
}

func (o LookupNetworkInsightsAccessScopeAnalysisResultOutput) AnalyzedEniCount() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupNetworkInsightsAccessScopeAnalysisResult) *int { return v.AnalyzedEniCount }).(pulumi.IntPtrOutput)
}

func (o LookupNetworkInsightsAccessScopeAnalysisResultOutput) EndDate() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupNetworkInsightsAccessScopeAnalysisResult) *string { return v.EndDate }).(pulumi.StringPtrOutput)
}

func (o LookupNetworkInsightsAccessScopeAnalysisResultOutput) FindingsFound() NetworkInsightsAccessScopeAnalysisFindingsFoundPtrOutput {
	return o.ApplyT(func(v LookupNetworkInsightsAccessScopeAnalysisResult) *NetworkInsightsAccessScopeAnalysisFindingsFound {
		return v.FindingsFound
	}).(NetworkInsightsAccessScopeAnalysisFindingsFoundPtrOutput)
}

func (o LookupNetworkInsightsAccessScopeAnalysisResultOutput) NetworkInsightsAccessScopeAnalysisArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupNetworkInsightsAccessScopeAnalysisResult) *string {
		return v.NetworkInsightsAccessScopeAnalysisArn
	}).(pulumi.StringPtrOutput)
}

func (o LookupNetworkInsightsAccessScopeAnalysisResultOutput) NetworkInsightsAccessScopeAnalysisId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupNetworkInsightsAccessScopeAnalysisResult) *string {
		return v.NetworkInsightsAccessScopeAnalysisId
	}).(pulumi.StringPtrOutput)
}

func (o LookupNetworkInsightsAccessScopeAnalysisResultOutput) StartDate() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupNetworkInsightsAccessScopeAnalysisResult) *string { return v.StartDate }).(pulumi.StringPtrOutput)
}

func (o LookupNetworkInsightsAccessScopeAnalysisResultOutput) Status() NetworkInsightsAccessScopeAnalysisStatusPtrOutput {
	return o.ApplyT(func(v LookupNetworkInsightsAccessScopeAnalysisResult) *NetworkInsightsAccessScopeAnalysisStatus {
		return v.Status
	}).(NetworkInsightsAccessScopeAnalysisStatusPtrOutput)
}

func (o LookupNetworkInsightsAccessScopeAnalysisResultOutput) StatusMessage() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupNetworkInsightsAccessScopeAnalysisResult) *string { return v.StatusMessage }).(pulumi.StringPtrOutput)
}

func (o LookupNetworkInsightsAccessScopeAnalysisResultOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v LookupNetworkInsightsAccessScopeAnalysisResult) []aws.Tag { return v.Tags }).(aws.TagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupNetworkInsightsAccessScopeAnalysisResultOutput{})
}
