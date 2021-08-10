// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ec2

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinsightsanalysis.html
type NetworkInsightsAnalysis struct {
	pulumi.CustomResourceState

	AlternatePathHints NetworkInsightsAnalysisAlternatePathHintArrayOutput `pulumi:"alternatePathHints"`
	Explanations       NetworkInsightsAnalysisExplanationArrayOutput       `pulumi:"explanations"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinsightsanalysis.html#cfn-ec2-networkinsightsanalysis-filterinarns
	FilterInArns               pulumi.StringArrayOutput                        `pulumi:"filterInArns"`
	ForwardPathComponents      NetworkInsightsAnalysisPathComponentArrayOutput `pulumi:"forwardPathComponents"`
	NetworkInsightsAnalysisArn pulumi.StringOutput                             `pulumi:"networkInsightsAnalysisArn"`
	NetworkInsightsAnalysisId  pulumi.StringOutput                             `pulumi:"networkInsightsAnalysisId"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinsightsanalysis.html#cfn-ec2-networkinsightsanalysis-networkinsightspathid
	NetworkInsightsPathId pulumi.StringOutput                             `pulumi:"networkInsightsPathId"`
	NetworkPathFound      pulumi.BoolOutput                               `pulumi:"networkPathFound"`
	ReturnPathComponents  NetworkInsightsAnalysisPathComponentArrayOutput `pulumi:"returnPathComponents"`
	StartDate             pulumi.StringOutput                             `pulumi:"startDate"`
	Status                pulumi.StringOutput                             `pulumi:"status"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinsightsanalysis.html#cfn-ec2-networkinsightsanalysis-statusmessage
	StatusMessage pulumi.StringPtrOutput `pulumi:"statusMessage"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinsightsanalysis.html#cfn-ec2-networkinsightsanalysis-tags
	Tags aws.TagArrayOutput `pulumi:"tags"`
}

// NewNetworkInsightsAnalysis registers a new resource with the given unique name, arguments, and options.
func NewNetworkInsightsAnalysis(ctx *pulumi.Context,
	name string, args *NetworkInsightsAnalysisArgs, opts ...pulumi.ResourceOption) (*NetworkInsightsAnalysis, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.NetworkInsightsPathId == nil {
		return nil, errors.New("invalid value for required argument 'NetworkInsightsPathId'")
	}
	var resource NetworkInsightsAnalysis
	err := ctx.RegisterResource("aws-native:EC2:NetworkInsightsAnalysis", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetNetworkInsightsAnalysis gets an existing NetworkInsightsAnalysis resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetNetworkInsightsAnalysis(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *NetworkInsightsAnalysisState, opts ...pulumi.ResourceOption) (*NetworkInsightsAnalysis, error) {
	var resource NetworkInsightsAnalysis
	err := ctx.ReadResource("aws-native:EC2:NetworkInsightsAnalysis", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering NetworkInsightsAnalysis resources.
type networkInsightsAnalysisState struct {
}

type NetworkInsightsAnalysisState struct {
}

func (NetworkInsightsAnalysisState) ElementType() reflect.Type {
	return reflect.TypeOf((*networkInsightsAnalysisState)(nil)).Elem()
}

type networkInsightsAnalysisArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinsightsanalysis.html#cfn-ec2-networkinsightsanalysis-filterinarns
	FilterInArns []string `pulumi:"filterInArns"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinsightsanalysis.html#cfn-ec2-networkinsightsanalysis-networkinsightspathid
	NetworkInsightsPathId string `pulumi:"networkInsightsPathId"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinsightsanalysis.html#cfn-ec2-networkinsightsanalysis-statusmessage
	StatusMessage *string `pulumi:"statusMessage"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinsightsanalysis.html#cfn-ec2-networkinsightsanalysis-tags
	Tags []aws.Tag `pulumi:"tags"`
}

// The set of arguments for constructing a NetworkInsightsAnalysis resource.
type NetworkInsightsAnalysisArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinsightsanalysis.html#cfn-ec2-networkinsightsanalysis-filterinarns
	FilterInArns pulumi.StringArrayInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinsightsanalysis.html#cfn-ec2-networkinsightsanalysis-networkinsightspathid
	NetworkInsightsPathId pulumi.StringInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinsightsanalysis.html#cfn-ec2-networkinsightsanalysis-statusmessage
	StatusMessage pulumi.StringPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinsightsanalysis.html#cfn-ec2-networkinsightsanalysis-tags
	Tags aws.TagArrayInput
}

func (NetworkInsightsAnalysisArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*networkInsightsAnalysisArgs)(nil)).Elem()
}

type NetworkInsightsAnalysisInput interface {
	pulumi.Input

	ToNetworkInsightsAnalysisOutput() NetworkInsightsAnalysisOutput
	ToNetworkInsightsAnalysisOutputWithContext(ctx context.Context) NetworkInsightsAnalysisOutput
}

func (*NetworkInsightsAnalysis) ElementType() reflect.Type {
	return reflect.TypeOf((*NetworkInsightsAnalysis)(nil))
}

func (i *NetworkInsightsAnalysis) ToNetworkInsightsAnalysisOutput() NetworkInsightsAnalysisOutput {
	return i.ToNetworkInsightsAnalysisOutputWithContext(context.Background())
}

func (i *NetworkInsightsAnalysis) ToNetworkInsightsAnalysisOutputWithContext(ctx context.Context) NetworkInsightsAnalysisOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NetworkInsightsAnalysisOutput)
}

type NetworkInsightsAnalysisOutput struct{ *pulumi.OutputState }

func (NetworkInsightsAnalysisOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*NetworkInsightsAnalysis)(nil))
}

func (o NetworkInsightsAnalysisOutput) ToNetworkInsightsAnalysisOutput() NetworkInsightsAnalysisOutput {
	return o
}

func (o NetworkInsightsAnalysisOutput) ToNetworkInsightsAnalysisOutputWithContext(ctx context.Context) NetworkInsightsAnalysisOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(NetworkInsightsAnalysisOutput{})
}
