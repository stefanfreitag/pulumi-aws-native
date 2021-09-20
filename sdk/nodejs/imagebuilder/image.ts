// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource schema for AWS::ImageBuilder::Image
 */
export class Image extends pulumi.CustomResource {
    /**
     * Get an existing Image resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Image {
        return new Image(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:imagebuilder:Image';

    /**
     * Returns true if the given object is an instance of Image.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Image {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Image.__pulumiType;
    }

    /**
     * The Amazon Resource Name (ARN) of the image.
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * The Amazon Resource Name (ARN) of the container recipe that defines how images are configured and tested.
     */
    public readonly containerRecipeArn!: pulumi.Output<string | undefined>;
    /**
     * The Amazon Resource Name (ARN) of the distribution configuration.
     */
    public readonly distributionConfigurationArn!: pulumi.Output<string | undefined>;
    /**
     * Collects additional information about the image being created, including the operating system (OS) version and package list.
     */
    public readonly enhancedImageMetadataEnabled!: pulumi.Output<boolean | undefined>;
    /**
     * The AMI ID of the EC2 AMI in current region.
     */
    public /*out*/ readonly imageId!: pulumi.Output<string>;
    /**
     * The Amazon Resource Name (ARN) of the image recipe that defines how images are configured, tested, and assessed.
     */
    public readonly imageRecipeArn!: pulumi.Output<string | undefined>;
    /**
     * The image tests configuration used when creating this image.
     */
    public readonly imageTestsConfiguration!: pulumi.Output<outputs.imagebuilder.ImageImageTestsConfiguration | undefined>;
    /**
     * The Amazon Resource Name (ARN) of the infrastructure configuration.
     */
    public readonly infrastructureConfigurationArn!: pulumi.Output<string | undefined>;
    /**
     * The name of the image.
     */
    public /*out*/ readonly name!: pulumi.Output<string>;
    /**
     * The tags associated with the image.
     */
    public readonly tags!: pulumi.Output<any | undefined>;

    /**
     * Create a Image resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: ImageArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            inputs["containerRecipeArn"] = args ? args.containerRecipeArn : undefined;
            inputs["distributionConfigurationArn"] = args ? args.distributionConfigurationArn : undefined;
            inputs["enhancedImageMetadataEnabled"] = args ? args.enhancedImageMetadataEnabled : undefined;
            inputs["imageRecipeArn"] = args ? args.imageRecipeArn : undefined;
            inputs["imageTestsConfiguration"] = args ? args.imageTestsConfiguration : undefined;
            inputs["infrastructureConfigurationArn"] = args ? args.infrastructureConfigurationArn : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["arn"] = undefined /*out*/;
            inputs["imageId"] = undefined /*out*/;
            inputs["name"] = undefined /*out*/;
        } else {
            inputs["arn"] = undefined /*out*/;
            inputs["containerRecipeArn"] = undefined /*out*/;
            inputs["distributionConfigurationArn"] = undefined /*out*/;
            inputs["enhancedImageMetadataEnabled"] = undefined /*out*/;
            inputs["imageId"] = undefined /*out*/;
            inputs["imageRecipeArn"] = undefined /*out*/;
            inputs["imageTestsConfiguration"] = undefined /*out*/;
            inputs["infrastructureConfigurationArn"] = undefined /*out*/;
            inputs["name"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(Image.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a Image resource.
 */
export interface ImageArgs {
    /**
     * The Amazon Resource Name (ARN) of the container recipe that defines how images are configured and tested.
     */
    containerRecipeArn?: pulumi.Input<string>;
    /**
     * The Amazon Resource Name (ARN) of the distribution configuration.
     */
    distributionConfigurationArn?: pulumi.Input<string>;
    /**
     * Collects additional information about the image being created, including the operating system (OS) version and package list.
     */
    enhancedImageMetadataEnabled?: pulumi.Input<boolean>;
    /**
     * The Amazon Resource Name (ARN) of the image recipe that defines how images are configured, tested, and assessed.
     */
    imageRecipeArn?: pulumi.Input<string>;
    /**
     * The image tests configuration used when creating this image.
     */
    imageTestsConfiguration?: pulumi.Input<inputs.imagebuilder.ImageImageTestsConfigurationArgs>;
    /**
     * The Amazon Resource Name (ARN) of the infrastructure configuration.
     */
    infrastructureConfigurationArn?: pulumi.Input<string>;
    /**
     * The tags associated with the image.
     */
    tags?: any;
}
