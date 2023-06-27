// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::SageMaker::EndpointConfig
 *
 * @deprecated EndpointConfig is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class EndpointConfig extends pulumi.CustomResource {
    /**
     * Get an existing EndpointConfig resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): EndpointConfig {
        pulumi.log.warn("EndpointConfig is deprecated: EndpointConfig is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new EndpointConfig(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:sagemaker:EndpointConfig';

    /**
     * Returns true if the given object is an instance of EndpointConfig.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is EndpointConfig {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === EndpointConfig.__pulumiType;
    }

    public readonly asyncInferenceConfig!: pulumi.Output<outputs.sagemaker.EndpointConfigAsyncInferenceConfig | undefined>;
    public readonly dataCaptureConfig!: pulumi.Output<outputs.sagemaker.EndpointConfigDataCaptureConfig | undefined>;
    public readonly endpointConfigName!: pulumi.Output<string | undefined>;
    public readonly explainerConfig!: pulumi.Output<outputs.sagemaker.EndpointConfigExplainerConfig | undefined>;
    public readonly kmsKeyId!: pulumi.Output<string | undefined>;
    public readonly productionVariants!: pulumi.Output<outputs.sagemaker.EndpointConfigProductionVariant[]>;
    public readonly shadowProductionVariants!: pulumi.Output<outputs.sagemaker.EndpointConfigProductionVariant[] | undefined>;
    public readonly tags!: pulumi.Output<outputs.sagemaker.EndpointConfigTag[] | undefined>;

    /**
     * Create a EndpointConfig resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated EndpointConfig is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: EndpointConfigArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("EndpointConfig is deprecated: EndpointConfig is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.productionVariants === undefined) && !opts.urn) {
                throw new Error("Missing required property 'productionVariants'");
            }
            resourceInputs["asyncInferenceConfig"] = args ? args.asyncInferenceConfig : undefined;
            resourceInputs["dataCaptureConfig"] = args ? args.dataCaptureConfig : undefined;
            resourceInputs["endpointConfigName"] = args ? args.endpointConfigName : undefined;
            resourceInputs["explainerConfig"] = args ? args.explainerConfig : undefined;
            resourceInputs["kmsKeyId"] = args ? args.kmsKeyId : undefined;
            resourceInputs["productionVariants"] = args ? args.productionVariants : undefined;
            resourceInputs["shadowProductionVariants"] = args ? args.shadowProductionVariants : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
        } else {
            resourceInputs["asyncInferenceConfig"] = undefined /*out*/;
            resourceInputs["dataCaptureConfig"] = undefined /*out*/;
            resourceInputs["endpointConfigName"] = undefined /*out*/;
            resourceInputs["explainerConfig"] = undefined /*out*/;
            resourceInputs["kmsKeyId"] = undefined /*out*/;
            resourceInputs["productionVariants"] = undefined /*out*/;
            resourceInputs["shadowProductionVariants"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(EndpointConfig.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a EndpointConfig resource.
 */
export interface EndpointConfigArgs {
    asyncInferenceConfig?: pulumi.Input<inputs.sagemaker.EndpointConfigAsyncInferenceConfigArgs>;
    dataCaptureConfig?: pulumi.Input<inputs.sagemaker.EndpointConfigDataCaptureConfigArgs>;
    endpointConfigName?: pulumi.Input<string>;
    explainerConfig?: pulumi.Input<inputs.sagemaker.EndpointConfigExplainerConfigArgs>;
    kmsKeyId?: pulumi.Input<string>;
    productionVariants: pulumi.Input<pulumi.Input<inputs.sagemaker.EndpointConfigProductionVariantArgs>[]>;
    shadowProductionVariants?: pulumi.Input<pulumi.Input<inputs.sagemaker.EndpointConfigProductionVariantArgs>[]>;
    tags?: pulumi.Input<pulumi.Input<inputs.sagemaker.EndpointConfigTagArgs>[]>;
}
