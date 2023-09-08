// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package iottwinmaker

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource schema for AWS::IoTTwinMaker::Scene
type Scene struct {
	pulumi.CustomResourceState

	// The ARN of the scene.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// A list of capabilities that the scene uses to render.
	Capabilities pulumi.StringArrayOutput `pulumi:"capabilities"`
	// The relative path that specifies the location of the content definition file.
	ContentLocation pulumi.StringOutput `pulumi:"contentLocation"`
	// The date and time when the scene was created.
	CreationDateTime pulumi.StringOutput `pulumi:"creationDateTime"`
	// The description of the scene.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// A key-value pair of generated scene metadata for the scene.
	GeneratedSceneMetadata pulumi.AnyOutput `pulumi:"generatedSceneMetadata"`
	// The ID of the scene.
	SceneId pulumi.StringOutput `pulumi:"sceneId"`
	// A key-value pair of scene metadata for the scene.
	SceneMetadata pulumi.AnyOutput `pulumi:"sceneMetadata"`
	// A key-value pair to associate with a resource.
	Tags pulumi.AnyOutput `pulumi:"tags"`
	// The date and time of the current update.
	UpdateDateTime pulumi.StringOutput `pulumi:"updateDateTime"`
	// The ID of the scene.
	WorkspaceId pulumi.StringOutput `pulumi:"workspaceId"`
}

// NewScene registers a new resource with the given unique name, arguments, and options.
func NewScene(ctx *pulumi.Context,
	name string, args *SceneArgs, opts ...pulumi.ResourceOption) (*Scene, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ContentLocation == nil {
		return nil, errors.New("invalid value for required argument 'ContentLocation'")
	}
	if args.SceneId == nil {
		return nil, errors.New("invalid value for required argument 'SceneId'")
	}
	if args.WorkspaceId == nil {
		return nil, errors.New("invalid value for required argument 'WorkspaceId'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"sceneId",
		"workspaceId",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Scene
	err := ctx.RegisterResource("aws-native:iottwinmaker:Scene", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetScene gets an existing Scene resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetScene(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SceneState, opts ...pulumi.ResourceOption) (*Scene, error) {
	var resource Scene
	err := ctx.ReadResource("aws-native:iottwinmaker:Scene", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Scene resources.
type sceneState struct {
}

type SceneState struct {
}

func (SceneState) ElementType() reflect.Type {
	return reflect.TypeOf((*sceneState)(nil)).Elem()
}

type sceneArgs struct {
	// A list of capabilities that the scene uses to render.
	Capabilities []string `pulumi:"capabilities"`
	// The relative path that specifies the location of the content definition file.
	ContentLocation string `pulumi:"contentLocation"`
	// The description of the scene.
	Description *string `pulumi:"description"`
	// The ID of the scene.
	SceneId string `pulumi:"sceneId"`
	// A key-value pair of scene metadata for the scene.
	SceneMetadata interface{} `pulumi:"sceneMetadata"`
	// A key-value pair to associate with a resource.
	Tags interface{} `pulumi:"tags"`
	// The ID of the scene.
	WorkspaceId string `pulumi:"workspaceId"`
}

// The set of arguments for constructing a Scene resource.
type SceneArgs struct {
	// A list of capabilities that the scene uses to render.
	Capabilities pulumi.StringArrayInput
	// The relative path that specifies the location of the content definition file.
	ContentLocation pulumi.StringInput
	// The description of the scene.
	Description pulumi.StringPtrInput
	// The ID of the scene.
	SceneId pulumi.StringInput
	// A key-value pair of scene metadata for the scene.
	SceneMetadata pulumi.Input
	// A key-value pair to associate with a resource.
	Tags pulumi.Input
	// The ID of the scene.
	WorkspaceId pulumi.StringInput
}

func (SceneArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*sceneArgs)(nil)).Elem()
}

type SceneInput interface {
	pulumi.Input

	ToSceneOutput() SceneOutput
	ToSceneOutputWithContext(ctx context.Context) SceneOutput
}

func (*Scene) ElementType() reflect.Type {
	return reflect.TypeOf((**Scene)(nil)).Elem()
}

func (i *Scene) ToSceneOutput() SceneOutput {
	return i.ToSceneOutputWithContext(context.Background())
}

func (i *Scene) ToSceneOutputWithContext(ctx context.Context) SceneOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SceneOutput)
}

func (i *Scene) ToOutput(ctx context.Context) pulumix.Output[*Scene] {
	return pulumix.Output[*Scene]{
		OutputState: i.ToSceneOutputWithContext(ctx).OutputState,
	}
}

type SceneOutput struct{ *pulumi.OutputState }

func (SceneOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Scene)(nil)).Elem()
}

func (o SceneOutput) ToSceneOutput() SceneOutput {
	return o
}

func (o SceneOutput) ToSceneOutputWithContext(ctx context.Context) SceneOutput {
	return o
}

func (o SceneOutput) ToOutput(ctx context.Context) pulumix.Output[*Scene] {
	return pulumix.Output[*Scene]{
		OutputState: o.OutputState,
	}
}

// The ARN of the scene.
func (o SceneOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *Scene) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

// A list of capabilities that the scene uses to render.
func (o SceneOutput) Capabilities() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Scene) pulumi.StringArrayOutput { return v.Capabilities }).(pulumi.StringArrayOutput)
}

// The relative path that specifies the location of the content definition file.
func (o SceneOutput) ContentLocation() pulumi.StringOutput {
	return o.ApplyT(func(v *Scene) pulumi.StringOutput { return v.ContentLocation }).(pulumi.StringOutput)
}

// The date and time when the scene was created.
func (o SceneOutput) CreationDateTime() pulumi.StringOutput {
	return o.ApplyT(func(v *Scene) pulumi.StringOutput { return v.CreationDateTime }).(pulumi.StringOutput)
}

// The description of the scene.
func (o SceneOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Scene) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// A key-value pair of generated scene metadata for the scene.
func (o SceneOutput) GeneratedSceneMetadata() pulumi.AnyOutput {
	return o.ApplyT(func(v *Scene) pulumi.AnyOutput { return v.GeneratedSceneMetadata }).(pulumi.AnyOutput)
}

// The ID of the scene.
func (o SceneOutput) SceneId() pulumi.StringOutput {
	return o.ApplyT(func(v *Scene) pulumi.StringOutput { return v.SceneId }).(pulumi.StringOutput)
}

// A key-value pair of scene metadata for the scene.
func (o SceneOutput) SceneMetadata() pulumi.AnyOutput {
	return o.ApplyT(func(v *Scene) pulumi.AnyOutput { return v.SceneMetadata }).(pulumi.AnyOutput)
}

// A key-value pair to associate with a resource.
func (o SceneOutput) Tags() pulumi.AnyOutput {
	return o.ApplyT(func(v *Scene) pulumi.AnyOutput { return v.Tags }).(pulumi.AnyOutput)
}

// The date and time of the current update.
func (o SceneOutput) UpdateDateTime() pulumi.StringOutput {
	return o.ApplyT(func(v *Scene) pulumi.StringOutput { return v.UpdateDateTime }).(pulumi.StringOutput)
}

// The ID of the scene.
func (o SceneOutput) WorkspaceId() pulumi.StringOutput {
	return o.ApplyT(func(v *Scene) pulumi.StringOutput { return v.WorkspaceId }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*SceneInput)(nil)).Elem(), &Scene{})
	pulumi.RegisterOutputType(SceneOutput{})
}
