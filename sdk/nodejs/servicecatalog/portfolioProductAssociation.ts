// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::ServiceCatalog::PortfolioProductAssociation
 *
 * @deprecated PortfolioProductAssociation is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class PortfolioProductAssociation extends pulumi.CustomResource {
    /**
     * Get an existing PortfolioProductAssociation resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): PortfolioProductAssociation {
        pulumi.log.warn("PortfolioProductAssociation is deprecated: PortfolioProductAssociation is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new PortfolioProductAssociation(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:servicecatalog:PortfolioProductAssociation';

    /**
     * Returns true if the given object is an instance of PortfolioProductAssociation.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is PortfolioProductAssociation {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === PortfolioProductAssociation.__pulumiType;
    }

    public readonly acceptLanguage!: pulumi.Output<string | undefined>;
    public readonly portfolioId!: pulumi.Output<string>;
    public readonly productId!: pulumi.Output<string>;
    public readonly sourcePortfolioId!: pulumi.Output<string | undefined>;

    /**
     * Create a PortfolioProductAssociation resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated PortfolioProductAssociation is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: PortfolioProductAssociationArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("PortfolioProductAssociation is deprecated: PortfolioProductAssociation is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.portfolioId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'portfolioId'");
            }
            if ((!args || args.productId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'productId'");
            }
            inputs["acceptLanguage"] = args ? args.acceptLanguage : undefined;
            inputs["portfolioId"] = args ? args.portfolioId : undefined;
            inputs["productId"] = args ? args.productId : undefined;
            inputs["sourcePortfolioId"] = args ? args.sourcePortfolioId : undefined;
        } else {
            inputs["acceptLanguage"] = undefined /*out*/;
            inputs["portfolioId"] = undefined /*out*/;
            inputs["productId"] = undefined /*out*/;
            inputs["sourcePortfolioId"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(PortfolioProductAssociation.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a PortfolioProductAssociation resource.
 */
export interface PortfolioProductAssociationArgs {
    acceptLanguage?: pulumi.Input<string>;
    portfolioId: pulumi.Input<string>;
    productId: pulumi.Input<string>;
    sourcePortfolioId?: pulumi.Input<string>;
}
